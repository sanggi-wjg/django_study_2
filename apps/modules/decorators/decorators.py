import functools
from typing import Callable

from apps.modules.exceptions.exceptions import brief_error
from apps.modules.utils.colorful import error
from apps.modules.utils.logger import Logger


def catch_error_basic(func: Callable):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)

        except Exception:
            err = brief_error()
            error(err)
            logger = Logger.get_logger('all')
            logger.error(err)

    return wrapper


def catch_error(logger_name: str = 'all'):
    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except Exception:
                err = brief_error()
                error(err)
                logger = Logger.get_logger(logger_name)
                logger.error(err)

        return wrapper

    return decorator
