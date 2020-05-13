import logging
from app import settings


LOG_FORMATTER = logging.Formatter(settings.LOG_FORMATTER_STRING)
logger = logging.getLogger(settings.APP_NAME)


def stream_log_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(LOG_FORMATTER)
    return stream_handler


def file_log_handler():
    file_handler = logging.FileHandler(settings.LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(LOG_FORMATTER)
    return file_handler
