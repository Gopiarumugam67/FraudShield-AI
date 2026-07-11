"""
Centralized logging configuration for FraudShield AI.

Every module in the project should use this logger instead of print().
"""

import logging
from pathlib import Path

from app.config.settings import settings


def setup_logger(name: str = "FraudShieldAI") -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name: Name of the logger.

    Returns:
        Configured logger instance.
    """

    # Create logs directory if it doesn't exist
    log_directory = Path(settings.log_dir)
    log_directory.mkdir(parents=True, exist_ok=True)

    log_file = log_directory / "application.log"

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, settings.log_level.upper()))

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


logger = setup_logger()