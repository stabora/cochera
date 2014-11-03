# -*- coding: utf-8 -*-

"""
Django settings for mi  io project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0+zr84p6%9jorcxxxo%7^s!wh5dszm__*i%w%pqlq&*t@jc4&u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suitlocale',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'cochera',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'python.urls'

WSGI_APPLICATION = 'python.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'cochera',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'cochera',
        'PASSWORD': 'cochera'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/cochera/static/'


##############################
# Custom configurations
##############################

BASE_URL = ''
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static/')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'cochera/templates'),
)

# Django Suit Theme

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'cochera.contexts.baseurl',
    'cochera.contexts.appname',
)

SUIT_CONFIG = {
    'ADMIN_NAME': 'Cochera - Administración',
    'SEARCH_URL': BASE_URL + '/cochera/lugar/',
    'MENU_ICONS': {
       'sites': 'icon-leaf',
       'auth': 'icon-lock',
    },
    'MENU': (
        'sites',
        {'app': 'cochera', 'icon':'icon-map-marker', 'models': ('lugar', 'titular', 'pago', 'gasto')},
        '-',
        {'label': u'Añadir pago', 'icon': 'icon-plus-sign', 'permissions': 'cochera.add_pago', 'url': BASE_URL + '/cochera/pago/add'},
        {'label': u'Añadir gasto', 'icon': 'icon-plus-sign', 'permissions': 'cochera.add_gasto', 'url': BASE_URL + '/cochera/gasto/add'},
        '-',
        {'label': u'Grilla anual', 'icon': 'icon-calendar', 'permissions': 'cochera.add_pago', 'url': BASE_URL + '/cochera/tabla'},
        {'label': u'Plano', 'icon': 'icon-globe', 'permissions': 'cochera.add_pago', 'url': BASE_URL + '/cochera/plano'},
        '-',
        {'label': 'Configuracion', 'app': 'cochera', 'icon':'icon-wrench', 'models': ('parametro', 'categoriagasto')},
        {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    ),
}
