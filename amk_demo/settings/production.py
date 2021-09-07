from django.contrib.messages import constants

from .base import *

DEBUG = False
MESSAGE_LEVEL = constants.SUCCESS

STATIC_ROOT = os.path.join(BASE_DIR, "static")

ALLOWED_HOSTS = [
]

DATABASES = {
}

LOGGING = {
    'version'                 : 1,
    'disable_existing_loggers': False,  # Do not set True.
    'formatters'              : {
        'simple': {
            'format': LOG_FORMAT_SIMPLE
        },
        'basic' : {
            'format': LOG_FORMAT_BASIC
        }
    },
    'filters'                 : {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true' : {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers'                : {
        'server_file' : {
            'class'      : 'logging.handlers.RotatingFileHandler',
            'level'      : 'WARNING',
            'backupCount': LOG_FILE_ROTATE_COUNT,
            'maxBytes'   : LOG_FILE_SIZE,
            'formatter'  : 'basic',
            'filename'   : LOG_SERVER_FILE
        },
        'request_file': {
            'class'      : 'logging.handlers.RotatingFileHandler',
            'level'      : 'WARNING',
            'backupCount': LOG_FILE_ROTATE_COUNT,
            'maxBytes'   : LOG_FILE_SIZE,
            'formatter'  : 'basic',
            'filename'   : LOG_REQUEST_FILE
        },
    },
    'loggers'                 : {
        'django.server'     : {
            'level'    : 'WARNING',
            'handlers' : ['server_file'],
            'propagate': False,
        },
        'django.security.*' : {
            'level'    : 'WARNING',
            'handlers' : ['server_file'],
            'propagate': False,
        },
        'django.request'    : {
            'level'    : 'WARNING',
            'handlers' : ['request_file'],
            'propagate': False,
        },
    },
}
