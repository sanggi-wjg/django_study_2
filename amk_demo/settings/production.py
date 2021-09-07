from django.contrib.messages import constants

from .base import *

DEBUG = False
MESSAGE_LEVEL = constants.SUCCESS

STATIC_ROOT = os.path.join(BASE_DIR, "static")

ALLOWED_HOSTS = [
]

DATABASES = {
}
