from django.conf import settings
from colorful_print import color


def colorful_dispatcher(c: str, msg: str, *args, **kwargs):
    if settings.DEBUG:
        dispatch = getattr(color, c)
        dispatch(msg, *args, **kwargs)


def debug(msg: str, *args, **kwargs):
    colorful_dispatcher('cyan', msg, *args, **kwargs)


def info(msg: str, *args, **kwargs):
    colorful_dispatcher('green', msg, *args, **kwargs)


def warning(msg: str, *args, **kwargs):
    colorful_dispatcher('yellow', msg, *args, **kwargs)


def error(msg: str, *args, **kwargs):
    colorful_dispatcher('red', msg, *args, **kwargs)
