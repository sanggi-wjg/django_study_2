import functools
from typing import Callable

from apps.modules.exceptions.exceptions import brief_error
from apps.modules.utils.colorful import error


def catch_error(func: Callable):
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)

        except Exception:
            err = brief_error()
            error(err)

    return wrapper


def param_deco(param = '?'):
    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            try:
                return func(request, *args, **kwargs)
            except Exception as e:
                err = brief_error()
                error(err)

        return wrapper

    return decorator
