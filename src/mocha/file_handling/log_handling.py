import os
import logging
import logging.config
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Create a directory for logs if it doesn't exist
log_directory = os.path.join('src', 'mocha', 'logs')
os.makedirs(log_directory, exist_ok=True)

# Create a non-root named logger
logger = logging.getLogger("main")

# Flag to check if logging has been set up
logging_setup_done = False

def setup_logging(default_level=logging.INFO):
    """Setup logging configuration if not already configured."""
    global logging_setup_done

    # Check if logging is already configured
    if logger.hasHandlers():
        logger.info("Logging is already configured. Skipping setup.")
        return  # Exit the function if logging is already configured

    # Create a dynamic log file name based on the current date
    log_file_name = f"app_{datetime.now().strftime('%Y-%m-%d')}.log"
    
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": default_level
            },
            "rotating_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(log_directory, log_file_name),
                "maxBytes": 5 * 1024 * 1024,  # 5 MB
                "backupCount": 5,
                "formatter": "simple",
                "level": logging.INFO
            }
        },
        "loggers": {
            "main": {
                "level": default_level,
                "handlers": ["console", "rotating_file"],
                "propagate": False
            }
        }
    }

    # Configure logging using the defined configuration
    try:
        logging.config.dictConfig(config)
        logging_setup_done = True  # Set the flag to indicate logging is set up
        logger.info("Logging setup complete.")
    except Exception as e:
        logger.error(f"Error configuring logging: {e}")

def get_logger():
    """Return the configured logger."""
    return logger

# Call the setup_logging function to configure logging
setup_logging()

# Example message usage of the logger
# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")