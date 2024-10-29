import os
import asyncio
import configparser
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import Router
from aiogram.types import ContentType

config = configparser.ConfigParser()
config.read('config.ini')

TELEGRAM_BOT_TOKEN = config['telegram']['bot_token']
TELEGRAM_TIMEOUT = int(config['telegram']['timeout'])
DOWNLOADS_FOLDER = config['paths']['downloads_folder']

bot = Bot(token=TELEGRAM_BOT_TOKEN, timeout=TELEGRAM_TIMEOUT)
dp = Dispatcher()
router = Router()

os.makedirs(DOWNLOADS_FOLDER, exist_ok=True)


@router.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Надішліть мені файл, і я збережу його.")


@router.message(lambda message: message.content_type == ContentType.DOCUMENT)
async def handle_document(message: types.Message):
    file_info = await bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    file_name = message.document.file_name

    downloaded_file = await bot.download_file(file_path)
    save_path = os.path.join(DOWNLOADS_FOLDER, file_name)

    with open(save_path, "wb") as file:
        file.write(downloaded_file.read())

    await message.reply(f"Файл збережено як '{file_name}' в папці '{DOWNLOADS_FOLDER}'.")


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())