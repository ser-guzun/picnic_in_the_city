import logging
import sys

from src.settings import Settings


def setup_logger(logger_name: str, log_file: str, settings: Settings):
    logger = logging.getLogger(logger_name)

    handler_stdout = logging.StreamHandler(stream=sys.stdout)
    handler_stdout.setFormatter(logging.Formatter(fmt=settings.LOG_FORMAT))

    file_handler = logging.FileHandler(
        "{0}/{1}.log".format(settings.LOG_PATH, log_file)
    )
    file_handler.setFormatter(logging.Formatter(fmt=settings.LOG_FORMAT))
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(logging.Formatter(fmt=settings.LOG_FORMAT))
    logger.addHandler(console_handler)

    logger.setLevel(settings.LOG_LEVEL)
