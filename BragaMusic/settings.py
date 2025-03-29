import os
from pathlib import Path

import dj_database_url



#load_dotenv() # Carrega as variaveis do .env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# if os.environ.get('SECRET_KEY'):
#    SECRET_KEY = os.environ.get('SECRET_KEY')
# else:
#    SECRET_KEY = 'm0(f51&nilbj_)m+^wog@3lw3-posmb8^)mx3_%&e+jor4t*t#'

#SECRET_KEY = os.environ.get('SECRET_KEY', 'm0(f51&nilbj_)m+^wog@3lw3-posmb8^)mx3_%&e+jor4t*t#')

#SECRET_KEY = 'm0(f51&nilbj_)m+^wog@3lw3-posmb8^)mx3_%&e+jor4t*t#'
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True
#DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'


# if os.environ.get('RENDER'):
#     ALLOWED_HOSTS = ['*']  # Ou seus hosts específicos
    
ALLOWED_HOSTS = ['*']  # Substitua pelo seu host no Render

# else:
#     ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Hosts para desenvolvimento local

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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




# PROD = os.environ.get('PROD')

# # Configurações para ambiente de produção (Render)
# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }

PROD = os.environ.get('PROD')

if os.environ.get('RENDER'):
    # Configuração para o banco de dados do Render
    DATABASE_URL = "postgresql://bragamusic_db_user:1tkE7NdnTBEePa156iA2O3quhYScVDB8@dpg-cvk3s9c9c44c738neog0-a/bragamusic_db"
    DATABASES = {
        'default': dj_database_url.config(default=DATABASE_URL)
    }
else:
    # Configuração para desenvolvimento local (se necessário)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Ou outro banco de dados local
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# ... (restant





AUTH_USER_MODEL = "instrumento.Cliente"

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


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

