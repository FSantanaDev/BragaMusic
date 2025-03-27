from pathlib import Path
import os
import json

BASE_DIR = Path(__file__).resolve().parent.parent


#SECRET_KEY = 'm0(f51&nilbj_)m+^wog@3lw3-posmb8^)mx3_%&e+jor4t*t#'
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True
#DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']  # Apenas para testes

MERCADO_PAGO_PUBLIC_KEY = "APP_USR-aaa24b62-41e7-443a-82ff-f737cab8f01d"
MERCADO_PAGO_ACCESS_TOKEN = "APP_USR-5090906557242439-031118-de20df38d823da6bbefda51c345df995-2319930959"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'instrumento',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BragaMusic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'BragaMusic.wsgi.app'
#WSGI_APPLICATION = 'BragaMusic.wsgi.application'


PROD = os.environ.get('PROD')

if PROD == '1':
    # Configurações para produção
    DATABASE_OPTIONS_RAW = os.environ.get('DATABASE_OPTIONS')
    DATABASE_OPTIONS = json.loads(DATABASE_OPTIONS_RAW) if DATABASE_OPTIONS_RAW else {"sslmode": "require"}

    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASE_ENGINE'),
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': os.environ.get('DATABASE_PORT'),
            'OPTIONS': DATABASE_OPTIONS,
        }
    }
else:
    # Configurações para desenvolvimento local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

AUTH_USER_MODEL = "instrumento.Cliente"

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

