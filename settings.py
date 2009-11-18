# -*- coding: utf-8 -*-
# Django settings for pythoncampus project.

import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vanderson Mota', 'vanderson.mota@gmail.com'),
    ('Vinícius Chagas', 'vinimaster@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'pythoncampus'
DATABASE_USER = 'pythoncampus'
DATABASE_PASSWORD = 'lapela'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'


TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'r&e+fl098tu8^n)rpyiw!90_(b2yb&_ia^r(xn&#75@oko149q'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'pythoncampus.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'pythoncampus.inscricoes',
#    'windmill',
)

EMAIL_HOST="yoda.iff.edu.br"
EMAIL_PORT="25"
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=False
