from django.contrib.messages import constants

from .base import *

DEBUG = True
MESSAGE_LEVEL = constants.DEBUG
# TEST_RUNNER = 'amk_demo.test_runner.TestRunner'

ALLOWED_HOSTS = [
    'localhost'
]

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME'  : BASE_DIR / 'db.sqlite3',
    }
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
        'console'     : {
            'class'  : 'logging.StreamHandler',
            'level'  : 'DEBUG',
            'filters': ['require_debug_true'],
        },
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
        'db_file'     : {
            'class'      : 'logging.handlers.RotatingFileHandler',
            'level'      : 'DEBUG',
            'backupCount': LOG_FILE_ROTATE_COUNT,
            'maxBytes'   : LOG_FILE_SIZE,
            'formatter'  : 'basic',
            'filename'   : LOG_DATABASE_FILE
        },
    },
    'loggers'                 : {
        'django.server'     : {
            'level'    : 'DEBUG',
            'handlers' : ['server_file', 'console'],
            'propagate': False,
        },
        'django.security.*' : {
            'level'    : 'DEBUG',
            'handlers' : ['server_file', 'console'],
            'propagate': False,
        },
        'django.request'    : {
            'level'    : 'DEBUG',
            'handlers' : ['request_file', 'console'],
            'propagate': False,
        },
        'django.db.backends': {
            'level'    : 'DEBUG',
            'handlers' : ['db_file'],
            'propagate': False,
        },
    },
}
