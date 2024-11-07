# Telegram Bot for RTorrent

A Telegram bot that handles file uploads and takes screenshots of RTorrent window.

## Configuration

Create a `config.ini` file in the root directory with the following structure:

```ini
[telegram]
# Your Telegram bot token from @BotFather
bot_token = YOUR_BOT_TOKEN_HERE
# Request timeout in seconds
timeout = 50
# Comma-separated list of allowed Telegram user IDs
allowed_users_ids = 123456789, 987654321
# Comma-separated list of allowed Telegram usernames (with @ symbol)
allowed_users_usernames = @username1, @username2

[paths]
# Folder where files will be downloaded
downloads_folder = D:\Downloads\telegram_files