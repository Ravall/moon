# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import platform
# _PATH - путь к manage.py
_PATH = os.path.abspath(os.path.dirname(__file__) + '/../')
DEBUG = platform.node() != 'sancta'
TEMPLATE_DEBUG = DEBUG
SERVER_EMAIL = 'valery.ravall@gmail.com'
ADMINS = (
    ('Ravall', SERVER_EMAIL),
)
MANAGERS = ADMINS

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'moon',
            'USER': 'moon_user',
            'PASSWORD': 'moon_user_password',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }
else:
    from moon.production import DATABASES



ALLOWED_HOSTS = []


TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(_PATH, '../', 'files', 'media'))
DIRECTORY = os.path.abspath(
    os.path.join(_PATH, '../', 'files', 'upload')
)
STATIC_ROOT = os.path.abspath(
    os.path.join(_PATH, '../', 'files', 'collected_static')
)
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'w&i03$)pza)u1f0bo4!^an(#r=&#g3@eo-g$a7eix60^*5hh=u'


# шаблоны
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(_PATH, '../', 'templates')
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'moon.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'moon.wsgi.application'




INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'frontend',
    'compressor'
)

# compressor
COMPRESS_REBUILD_TIMEOUT = 1
COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'min'
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    ('text/stylus', 'stylus < {infile} > {outfile}'),
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
