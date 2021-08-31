import logging

from amk_demo.settings.base import LOG_FORMAT_BASIC, LOG_FORMAT_THREAD
from modules.utils.common import get_DEBUG


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance


class Logger(Singleton):

    @staticmethod
    def get_logger(name: str, path: str = '', isThread: bool = False):
        logger = logging.getLogger(name)
        if get_DEBUG():
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        formatter = _get_log_formatter(isThread)
        fileHandler = _get_log_file_handler(name, path)
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        return logger


def _get_log_formatter(isThread: bool = False):
    if isThread:
        return logging.Formatter(LOG_FORMAT_THREAD)

    return logging.Formatter(LOG_FORMAT_BASIC)


def _get_log_file_handler(name: str, path: str = ''):
    # LOG_BASE_ROOT

    if path == '':
        return logging.FileHandler(name)

    return logging.FileHandler(path)
