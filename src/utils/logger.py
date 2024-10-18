import logging
from logging.handlers import RotatingFileHandler
import os
import sys

# --- Environment Variables and Configuration ---

# Load environment variables using dotenv:
from dotenv import load_dotenv
load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

# --- Logger Configuration ---

logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, LOG_LEVEL))

# --- File Handler Configuration ---

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s')

# --- File Handler Configuration ---

if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler('logs/ai_connector.log', maxBytes=1024 * 1024 * 10, backupCount=5)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# --- Stream Handler Configuration (for console output) ---

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)