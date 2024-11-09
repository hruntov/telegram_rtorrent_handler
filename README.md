# Telegram Bot for RTorrent

A Telegram bot that handles file uploads to different folders and takes screenshots of RTorrent session.

## Features
- Upload files to specific folders (Movies, Series, Other)
- Take screenshots of RTorrent screen session
- User authorization
- Custom keyboard interface

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
# Folders for different types of content
downloads_folder_for_other = /path/to/watch/folder
downloads_folder_for_movies = /path/to/movies/folder
downloads_folder_for_series = /path/to/series/folder

### Prerequisites
- Python 3.8 or higher
- Poetry (Python package manager)
- Screen utility for RTorrent

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/telegram_rtorrent_handler.git
    cd telegram_rtorrent_handler
    ```

2. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

3. Create and configure `config.ini` using the template above:
    ```ini
    [telegram]
    bot_token = YOUR_BOT_TOKEN_HERE
    timeout = 50
    allowed_users_ids = 123456789, 987654321
    allowed_users_usernames = @username1, @username2
    ```

4. Run the bot:
    ```bash
    poetry run python main.py
    ```
