import functools
from typing import Callable

from modules.utils.colorful import error
from modules.utils.common import brief_error
from modules.utils.logger import Logger


def catch_error(func: Callable):
    def wrapper(request, *args, **kwargs):
        logger = Logger.get_logger('all')
        try:
            return func(request, *args, **kwargs)

        except Exception:
            err = brief_error()
            error(err)
            logger.error(err)

    return wrapper


def deco_param_sample(logger_name: str = 'all'):
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
