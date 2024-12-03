from decouple import config

# Telegram API credentials
API_ID = config('API_ID', cast=int)  # API ID should be an integer
API_HASH = config('API_HASH')

# Telegram bot token
BOT_TOKEN = config('BOT_TOKEN')

# Other configuration variables
UPLOAD_DIR = config('UPLOAD_DIR', default='./uploads')
MAX_BATCH_SIZE = config('MAX_BATCH_SIZE', default=10, cast=int)
DEBUG_MODE = config('DEBUG_MODE', default=True, cast=bool)

# Network settings
TIMEOUT = config('TIMEOUT', default=60, cast=int)
RETRY_ATTEMPTS = config('RETRY_ATTEMPTS', default=3, cast=int)
