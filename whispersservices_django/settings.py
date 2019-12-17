"""
Django settings for whispersservices_django project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from django.utils.six import moves

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

CONFIG = moves.configparser.RawConfigParser(allow_no_value=True)
CONFIG.read('%s\settings.cfg' % SETTINGS_DIR)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('security', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG.get('general', 'DEBUG')
ADMIN_ENABLED = False

# ALLOWED_HOSTS = CONFIG.get('general', 'ALLOWED_HOSTS')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
APP_WHISPERS_URL = CONFIG.get('general', 'APP_WHISPERS_URL')

ENVIRONMENT = CONFIG.get('general', 'ENVIRONMENT')
SSL_CERT = SETTINGS_DIR + '/ca-bundle.crt'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple_history',
    'rest_framework',
    'corsheaders',
    'dry_rest_permissions',
    'whispersservices',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'whispersservices_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

WSGI_APPLICATION = 'whispersservices_django.wsgi.application'

EMAIL_BACKEND = CONFIG.get('email', 'EMAIL_BACKEND')
EMAIL_HOST = CONFIG.get('email', 'EMAIL_HOST')
EMAIL_HOST_PASSWORD = CONFIG.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = CONFIG.get('email', 'EMAIL_HOST_USER')
EMAIL_PORT = CONFIG.get('email', 'EMAIL_PORT')
EMAIL_USE_TLS = CONFIG.get('email', 'EMAIL_USE_TLS')
EMAIL_TIMEOUT = CONFIG.get('email', 'EMAIL_TIMEOUT')
DEFAULT_FROM_EMAIL = CONFIG.get('email', 'DEFAULT_FROM_EMAIL')
# EMAIL_HOST = '127.0.0.1'
# EMAIL_PORT = '25'
EMAIL_WHISPERS = CONFIG.get('email', 'EMAIL_WHISPERS')
EMAIL_NWHC_EPI = CONFIG.get('email', 'EMAIL_NWHC_EPI')

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('databases', 'ENGINE'),
        'NAME': CONFIG.get('databases', 'NAME'),
        'USER': CONFIG.get('databases', 'USER'),
        'PASSWORD': CONFIG.get('databases', 'PASSWORD'),
        'HOST': CONFIG.get('databases', 'HOST'),
        'PORT': CONFIG.get('databases', 'PORT'),
        #'CONN_MAX_AGE': CONFIG.get('databases', 'CONN_MAX_AGE'),
        'CONN_MAX_AGE': 60,
    }
}

AUTH_USER_MODEL = 'whispersservices.User'
GEONAMES_USERNAME = CONFIG.get('geonames', 'USERNAME')

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static/staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

CORS_ORIGIN_ALLOW_ALL = True

CELERY_IMPORTS = ['whispersservices.tasks']
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'rpc://'
# CELERY_TASK_ROUTES = {
#     'immediate_tasks.*': 'default',
#     'scheduled_tasks.*': 'beat'
# }
# CELERY_CREATE_MISSING_QUEUES = True
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_IGNORE_RESULT = False
# CELERY_TASK_IGNORE_RESULT = False
# CELERY_TRACK_STARTED = True
# CELERY_TASK_TRACK_STARTED = True