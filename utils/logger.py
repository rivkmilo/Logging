import os
import logging
from utils import DETAILED_LOGGER_PATH, LOGGER_NAME, SHORT_LOGGER_PATH

def _create_logs_folder():
    try:
        os.mkdir('logs')
    except FileExistsError as ex:
        pass

def _get_logger():
    _create_logs_folder()

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.INFO)

    short_logs_formatter = logging.Formatter('%(funcName)s in line %(lineno)d: %(message)s')
    short_logs_file_handler = logging.FileHandler(SHORT_LOGGER_PATH)
    short_logs_file_handler.setFormatter(short_logs_formatter)
    short_logs_file_handler.setLevel(logging.INFO)

    short_logs_stream_handler = logging.StreamHandler()
    short_logs_stream_handler.setFormatter(short_logs_formatter)
    short_logs_stream_handler.setLevel(logging.INFO)

    logger.addHandler(short_logs_file_handler)
    logger.addHandler(short_logs_stream_handler)

    detailed_logs_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s in line %(lineno)d: %(message)s')
    detailed_logs_file_handler = logging.FileHandler(DETAILED_LOGGER_PATH)
    detailed_logs_file_handler.setFormatter(detailed_logs_formatter)
    detailed_logs_file_handler.setLevel(logging.ERROR)

    logger.addHandler(detailed_logs_file_handler)
    return logger
