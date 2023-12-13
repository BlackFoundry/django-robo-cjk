"""
Django settings for djangodemo project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import environ
import pymysql
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import ignore_logger as sentry_sdk_ignore_logger

# https://github.com/joke2k/django-environ
env = environ.Env(
    DEBUG=(bool, False),
    DEBUG_TOOLBAR_SHOW=(bool, False),
    ROBOCJK_EXPORT_CANCEL_TIMEOUT=(int, 120),
    ROBOCJK_EXPORT_QUERIES_PAGINATION_LIMIT=(int, 500),
)
env_root = environ.Path(__file__) - 3  # get root of the project
env_path = env_root() + "/conf/env_settings"
# print(env_path)
environ.Env.read_env(env_path)

# sentry - https://sentry.io/black-foundry/
sentry_sdk.init(
    dsn=env("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    environment=env("SENTRY_ENVIRONMENT"),
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
sentry_sdk_ignore_logger("django.security.DisallowedHost")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

ENV_DIR = os.path.dirname(BASE_DIR)
# print(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

GIT_REPOSITORIES_PATH = env("GIT_REPOSITORIES_PATH")
GIT_USER_EMAIL = env("GIT_USER_EMAIL")
GIT_USER_NAME = env("GIT_USER_NAME")

JWT_SECRET = env("JWT_SECRET")
JWT_ALGORITHM = "HS256"

ROBOCJK_EXPORT_CANCEL_TIMEOUT = env("ROBOCJK_EXPORT_CANCEL_TIMEOUT")
ROBOCJK_EXPORT_QUERIES_PAGINATION_LIMIT = env("ROBOCJK_EXPORT_QUERIES_PAGINATION_LIMIT")

TEST_API_HOST = env("TEST_API_HOST")
TEST_API_USERNAME = env("TEST_API_USERNAME")
TEST_API_PASSWORD = env("TEST_API_PASSWORD")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

SITE_ID = 1

ADMINS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]

MANAGERS = [
    (env("ADMIN_NAME"), env("ADMIN_EMAIL")),
]


# Email server
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = "[development] " if DEBUG else "[production] "

DEFAULT_FROM_EMAIL = f"Black Foundry / RoboCJK <{EMAIL_HOST_USER}>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL


# Application definition

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    # 'django.contrib.sites',
    # 'django.contrib.sitemaps',
    "django.contrib.staticfiles",
    "corsheaders",
    "debug_toolbar",
    "django_json_widget",
    "extra_settings",
    "rangefilter",
    "robocjk",
    "django_cleanup.apps.CleanupConfig",
]

X_FRAME_OPTIONS = "SAMEORIGIN"

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.csrf",
                "django.template.context_processors.request",
            ],
        },
    },
]

# Security
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True

# Session
# https://docs.djangoproject.com/en/dev/ref/settings/#sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_AGE = 1209600 * 26  # (2 weeks * 26 = 52 weeks, in seconds)'
# SESSION_COOKIE_DOMAIN = ''
SESSION_COOKIE_SECURE = True


DATA_UPLOAD_MAX_NUMBER_FIELDS = None

WSGI_APPLICATION = "app.wsgi.application"

ROOT_URLCONF = "app.urls"

APPEND_SLASH = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": "",
        "PORT": "",
        "OPTIONS": {
            "charset": "utf8mb4",
        },
        #         'CONN_MAX_AGE': 0,
        #         'OPTIONS': {
        #             'connect_timeout': 60,
        #         }
    },
}

pymysql.version_info = (2, 1, 1)
pymysql.install_as_MySQLdb()

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", "English"),
    ("fr", "Français"),
    ("it", "Italiano"),
)
MULTILANGUAGE = len(LANGUAGES) > 1

# TIME_ZONE = 'UTC'
TIME_ZONE = "Europe/Paris"
USE_I18N = False
USE_L10N = False
USE_TZ = False


DATE_FORMAT = "Y/m/d"
# DATETIME_FORMAT = 'Y/m/d H:i:s.u'
DATETIME_FORMAT = "Y/m/d H:i:s"


# https://docs.djangoproject.com/en/3.1/ref/settings/#data-upload-max-memory-size
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440 * 4  # 10 MB

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = env("MEDIA_ROOT")

# Used for media served from CDN
MEDIA_HOST = env("MEDIA_HOST", default="")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = '/media/'
MEDIA_URL = MEDIA_HOST + "/media/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = env("STATIC_ROOT")

STATIC_HOST = env("STATIC_HOST", default="")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'
STATIC_URL = STATIC_HOST + "/static/"


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # VIRTUALENV_PATH +'/sources/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# if DEBUG:
#    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# else:
#    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = "robocjk.storage.ManifestStaticFilesStorageNotStrict"


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": ENV_DIR + "/cache/",
    },
    "logging": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": ENV_DIR + "/cache/logging/",
        "TIMEOUT": 3600,
    },
    "extra_settings": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": ENV_DIR + "/cache/settings/",
        "TIMEOUT": 60,
    },
}


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# import logging
# logger = logging.getLogger('app')
# logger.debug('message')


def get_app_logger(level_debug, level, propagate=False):
    handlers = [
        "console",
        "debug_file",
        "info_file",
        "warning_file",
        "error_file",
        "error_mail_admins",
    ]
    # handlers = ['console', 'debug_file', 'info_file', 'warning_file', 'error_file', 'mail_admins']
    logger_options = {
        "handlers": handlers,
        "level": level_debug if DEBUG else level,
        "propagate": propagate,
    }
    # print(logger_options)
    return logger_options


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "throttle": {
            "()": "robocjk.logging.ThrottleFilter",
            "timeout": 60 * 60 * 24,  # 1 day
        },
    },
    "formatters": {
        "simple": {"format": "%(asctime)s %(name)s [%(levelname)s]: %(message)s"},
        "verbose": {
            "format": "%(asctime)s %(name)s %(module)s %(process)d %(thread)d [%(levelname)s]: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "debug_file": {
            "level": "DEBUG",
            # 'class': 'logging.FileHandler',
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ENV_DIR + "/logs/django-debug.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 1,
            "formatter": "verbose",
        },
        #         'debug_queries_file': {
        #             'level': 'DEBUG',
        #             # 'class': 'logging.FileHandler',
        #             'class': 'logging.handlers.RotatingFileHandler',
        #             'filename': ENV_DIR + '/logs/django-mysql-debug.log',
        #             'maxBytes': 1024 * 1024 * 5, # 5 MB
        #             'backupCount': 1,
        #             'formatter':'verbose',
        #         },
        "info_file": {
            "level": "INFO",
            # 'class': 'logging.FileHandler',
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ENV_DIR + "/logs/django-info.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 1,
            "formatter": "verbose",
        },
        "warning_file": {
            "level": "WARNING",
            # 'class': 'logging.FileHandler',
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ENV_DIR + "/logs/django-warning.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 1,
            "formatter": "verbose",
        },
        "error_file": {
            "level": "ERROR",
            # 'class': 'logging.FileHandler',
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ENV_DIR + "/logs/django-error.log",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 1,
            "formatter": "verbose",
        },
        "error_mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["throttle"],
            "include_html": True,
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django": get_app_logger(level_debug="WARNING", level="ERROR"),
        #         'django.db.backends': {
        #             'handlers': ['debug_queries_file'],
        #             'level': 'DEBUG',
        #         },
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
        "app": get_app_logger(level_debug="WARNING", level="ERROR"),
        "robocjk": get_app_logger(level_debug="INFO", level="INFO"),
        "": get_app_logger(level_debug="WARNING", level="ERROR", propagate=False),
    },
}


# django-admin-rangefilter - https://github.com/silentsokolov/django-admin-rangefilter
ADMIN_RANGEFILTER_NONCE_ENABLED = False


# django-cors-headers
CORS_ORIGIN_WHITELIST = ("http://localhost:8000",)


# django-csp - https://django-csp.readthedocs.io/
CSP_DEFAULT_SRC = (
    "'self'",
    "'unsafe-inline'",
    "'unsafe-eval'",
    "data:",
    "blob:",
    # 'cdn.jsdelivr.net', 'use.fontawesome.com',
    "*.black-foundry.com",
    # '*.kxcdn.com',
    # '*.google.com', '*.googleapis.com', '*.gstatic.com',
    # '*.google-analytics.com', '*.doubleclick.net', '*.googletagmanager.com', '*.hotjar.com',
    # '*.youtube.com', '*.vimeo.com',
)


# django-debug-toolbar - https://pypi.python.org/pypi/django-debug-toolbar/
DEBUG_TOOLBAR_SHOW = env("DEBUG_TOOLBAR_SHOW")
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG_TOOLBAR_SHOW and DEBUG,
}
INTERNAL_IPS = ("127.0.0.1",)


# hashids - https://github.com/davidaurelio/hashids-python
HASHIDS_SALT = env("HASHIDS_SALT")
HASHIDS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
HASHIDS_MIN_LENGTH = 7
HASHIDS_OPTIONS = {
    "salt": HASHIDS_SALT,
    "alphabet": HASHIDS_ALPHABET,
    "min_length": HASHIDS_MIN_LENGTH,
}
