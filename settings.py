"""
Django settings for local_second project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import sys
import warnings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = PROJECT_ROOT

PROJECT_PATH = os.path.dirname(__file__).replace("\\", "/")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-my8*s-ef=zaf1c$6)j+vm!hq(mo1+4y#-2py%+5*%rtf2er-8h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "integration_utils",
    "integration_utils.bitrix24",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

X_FRAME_OPTIONS = "ALLOW-FROM https://b24-68oetn.bitrix24.ru"

# Database (оставьте пустым для переопределения в local_settings)
DATABASES = {}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройки CORS и CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://b24-68oetn.bitrix24.ru",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://56218ef983f3-8301993767665431593.ngrok-free.app",
]

# Импорт MuteLogger
try:
    from integration_utils.its_utils.mute_logger import MuteLogger

    ilogger = MuteLogger()
except ImportError:
    warnings.warn("integration_utils.its_utils.mute_logger not found")

# Локальные настройки
try:
    from local_settings import *
except ImportError:
    warnings.warn("create local_settings.py")

if not APP_SETTINGS:
    from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

    APP_SETTINGS = LocalSettingsClass(
        portal_domain="b24-68oetn.bitrix24.ru",
        app_domain="is_demo.it-solution.ru",
        app_name="post_currency",
        salt="df897hynj4b34u804b5n45bkl4b",
        secret_key="sfjbh40989034nk4j4389tfj",
        application_index_path="/",
    )
