import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
IMAGE_DIR = os.path.join(ROOT_DIR, 'imagefiles')
IMAGE_THIEF = os.path.join(IMAGE_DIR, 'thief-chan')

DISCORD_BOT_TOKEN = DEBUG = os.getenv("DISCORD_BOT_TOKEN", False)


# Reddit Configuration
REDDIT_APP_ID = DEBUG = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = DEBUG = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_ENABLED_SUBREDDITS = [
    'funny',
    'memes',
    'gaming',
    'jokes',
    'ffxiv',
    'chemicalreactiongifs'
]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'wtf',
]

# Permissions

MODERATOR_ROLE_NAME = "Mods", "Grand Poobah"