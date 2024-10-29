import os
import asyncio
import configparser
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import ContentType

from logger import activity_logger, error_logger


config = configparser.ConfigParser()
config.read('config.ini')

TELEGRAM_BOT_TOKEN = config['telegram']['bot_token']
TELEGRAM_TIMEOUT = int(config['telegram']['timeout'])
DOWNLOADS_FOLDER = config['paths']['downloads_folder']
ALLOWED_USERS_IDS = [
    int(user_id.strip()) for user_id in config['telegram']['allowed_users_ids'].split(',')]
ALLOWED_USERS_USERNAMES = [
    username.strip() for username in config['telegram']['allowed_users_usernames'].split(',')]

bot = Bot(token=TELEGRAM_BOT_TOKEN, timeout=TELEGRAM_TIMEOUT)
dp = Dispatcher()
router = Router()

os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message) -> None:
    """
    Sends a welcome message to the user when they send the /start or /help command.

    Args:
        message (types.Message): The message containing the command.

    """
    await message.reply("Привіт! Надішліть мені файл, і я збережу його.")


@router.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def handle_document(message: types.Message) -> None:
    """
    Handles incoming document messages.

    Args:
        message (types.Message): The message containing the document.

    """
    try:
        if await get_authorize(message):
            file_info = await bot.get_file(message.document.file_id)
            file_path = file_info.file_path
            file_name = message.document.file_name
            await download_file(message, file_path, file_name)
    except Exception as e:
        error_logger.error(f"Error handling document: {e}")
        await message.reply("Сталася помилка при обробці файлу.")


async def download_file(message: types.Message, file_path: str, file_name: str):
    """
    Downloads the file from the message and saves it to the specified folder.

    Args:
        message (types.Message): The message containing the document.
        file_path (str): The path of the file to download.
        file_name (str): The name of the file.

    """
    try:
        downloaded_file = await bot.download_file(file_path)
        save_path = os.path.join(DOWNLOADS_FOLDER, file_name)

        with open(save_path, "wb") as file:
            file.write(downloaded_file.read())
        activity_logger.info(
            f"File '{file_name}'saved in the '{DOWNLOADS_FOLDER}' directory "
            f"by user {message.from_user.username}."
        )
        await message.reply(f"Файл збережено як '{file_name}' в папці '{DOWNLOADS_FOLDER}'.")
    except Exception as e:
        error_logger.error(f"Error downloading file: {e}")
        await message.reply("Сталася помилка при завантаженні файлу.")


async def get_authorize(message: types.Message) -> bool:
    """
    Verifies if the user's ID or username is in the list of allowed users.
    If the user is not authorized, sends a message denying access.

    Args:
        message (types.Message): The message from the user.

    Returns:
        bool: True if the user is authorized, otherwise False.

    """
    user_id = message.from_user.id
    username = f"@{message.from_user.username}"

    if user_id in ALLOWED_USERS_IDS or username in ALLOWED_USERS_USERNAMES:
        return True

    error_logger.error(f"Authorization failed for user {username}")
    await message.reply("Ви не маєте дозволу надсилати файли.")
    return False


async def main() -> None:
    """
    The main function to start the bot.
    This function includes the router in the dispatcher and starts polling for updates.

    """
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
