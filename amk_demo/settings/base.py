"""
Django settings for amk_demo project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@mik0u4s*rt6=9m56zjm!@jq$osm3wju5%k%*&vy0p0k917!cz'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_plotly_dash.apps.DjangoPlotlyDashConfig',

    'dashboard',
    'file',
    'home',
    'sample',
    'user',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_plotly_dash.middleware.BaseMiddleware'
]

ROOT_URLCONF = 'amk_demo.urls'

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'builtins'          : ['apps.module.templatetags.help_tags']
        },
    },
]

WSGI_APPLICATION = 'amk_demo.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
LOGIN_URL = '/login'
INDEX_URL = '/'

# Secure
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Rest Framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions, or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Redis
CACHES = {
    "default": {
        "BACKEND" : "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.10.204:6379",
        "OPTIONS" : {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Log
LOG_BASE_ROOT = os.path.join(BASE_DIR, "logs")
LOG_DATABASE_FILE = os.path.join(LOG_BASE_ROOT, "database.log")
LOG_REQUEST_FILE = os.path.join(LOG_BASE_ROOT, "request.log")
LOG_SERVER_FILE = os.path.join(LOG_BASE_ROOT, "server.log")

LOG_FILE_ROTATE_COUNT = 50
LOG_FILE_SIZE = 1024 * 1024 * 20  # about 20 Mb

LOG_FORMAT_SIMPLE = '[%(asctime)s] %(message)s'
LOG_FORMAT_BASIC = '[%(levelname)s] [%(asctime)s] (%(name)s) %(message)s'
LOG_FORMAT_THREAD = '[%(levelname)s] [%(asctime)s] (%(name)s) (Id: %(thread)d, Name: %(threadName)s) %(message)s '

# https://docs.djangoproject.com/en/3.2/topics/logging/
