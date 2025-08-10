import logging
import os
from app.config import settings  # Load LOG_LEVEL, LOG_FILE from config


def get_logger(name: str) -> logging.Logger:
    """
    Creates a logger that outputs to both console and file.
    Log level comes from settings.LOG_LEVEL (default = INFO).
    """

    # Ensure logs directory exists
    os.makedirs(os.path.dirname(settings.LOG_FILE), exist_ok=True)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
        ch_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        ch.setFormatter(ch_formatter)
        logger.addHandler(ch)

        # File handler
        fh = logging.FileHandler(settings.LOG_FILE)
        fh.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))
        fh_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)

    return logger


# Manual test if run directly
if __name__ == "__main__":
    log = get_logger(__name__)
    log.info("Logger initialized successfully.")
    log.warning("Test warning message.")
    log.error("Test error message.")
