import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()


# Define o diretório base do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent


#SECRET_KEY = os.environ.get('DJANGO_SEECRET_KEY')
SECRET_KEY  = '&qsyews#8143n@9mkzj^7p@!x4ls8+7_=#&dh)iorz6*!c9b'   
# Modo de depuração.

# DEBUG = int(os.environ.get('DJANGO_DEBUG', default=0))
DEBUG = True

#ALLOWED_HOSTS =str(os.environ.get('DJANGO_ALLOWED_HOSTS')).split(',') # ou seus hosts específicos
#ALOWED_HOSTS = ["*"]
# Configurações do Mercado Pago
MERCADO_PAGO_PUBLIC_KEY = "APP_USR-aaa24b62-41e7-443a-82ff-f737cab8f01d"
MERCADO_PAGO_ACCESS_TOKEN = "APP_USR-5090906557242439-031118-de20df38d823da6bbefda51c345df995-2319930959"

# Aplicativos instalados no projeto Django.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'instrumento',  # Seu aplicativo
    'django.contrib.humanize',
]

# Middlewares do Django.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir arquivos estáticos em produção
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivo de configuração de URL raiz do projeto.
ROOT_URLCONF = 'BragaMusic.urls'

# Configurações de templates do Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Diretório de templates do projeto
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração do WSGI (Web Server Gateway Interface).
WSGI_APPLICATION = 'BragaMusic.wsgi.app'



# Configuração do banco de dados.
# Use variáveis de ambiente para a URL do banco de dados em produção.
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Modelo de usuário personalizado.
AUTH_USER_MODEL = "instrumento.Cliente"

# Validadores de senha.
# Você pode descomentar e personalizar isso em produção para aumentar a segurança.
AUTH_PASSWORD_VALIDATORS = []
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Configurações de internacionalização.
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos.
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Comente essa linha para previnir erros em alguns casos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório onde os arquivos estáticos são coletados
MEDIA_URL = '/media/'  # URL para arquivos de mídia (uploads do usuário)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório onde os arquivos de mídia são armazenados

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Outros diretórios onde os arquivos estáticos podem estar
]

# Configurações de logging
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
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO'),  # Use uma variável de ambiente para o nível de log
        },
    },
}

# Configuração do campo de ID automático padrão.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
