# utils.py
import configparser
import os
from typing import List


def load_config() -> configparser.ConfigParser:
    """Load configuration from config.ini file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def get_allowed_users_ids(config: configparser.ConfigParser) -> List[int]:
    """Get list of allowed user IDs from config."""
    return [
        int(user_id.strip())
        for user_id in config['telegram']['allowed_users_ids'].split(',')
    ]


def get_allowed_users_usernames(config: configparser.ConfigParser) -> List[str]:
    """Get list of allowed usernames from config."""
    return [
        username.strip()
        for username in config['telegram']['allowed_users_usernames'].split(',')
    ]


def create_download_folders(config: configparser.ConfigParser) -> None:
    """Create folders for downloads if they don't exist."""
    os.makedirs(config['paths']['downloads_folder_for_movies'], exist_ok=True)
    os.makedirs(config['paths']['downloads_folder_for_series'], exist_ok=True)
    os.makedirs(config['paths']['downloads_folder_for_other'], exist_ok=True)


# Constants
SCREENSHOT_BUTTON = "📸 Зробити знімок екрана"
MOVIE_BUTTON = "🎬 Фільм"
SERIES_BUTTON = "📺 Серіал"
OTHER_BUTTON = "📁 Інше"

# Load configuration
config = load_config()

# Bot configuration
TELEGRAM_BOT_TOKEN = config['telegram']['bot_token']
TELEGRAM_TIMEOUT = int(config['telegram']['timeout'])

# Paths configuration
DOWNLOADS_FOLDER_FOR_OTHER = config['paths']['downloads_folder_for_other']
DOWNLOADS_FOLDER_FOR_MOVIES = config['paths']['downloads_folder_for_movies']
DOWNLOADS_FOLDER_FOR_SERIES = config['paths']['downloads_folder_for_series']

# Users configuration
ALLOWED_USERS_IDS = get_allowed_users_ids(config)
ALLOWED_USERS_USERNAMES = get_allowed_users_usernames(config)
