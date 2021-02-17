from corsheaders.defaults import default_headers
from decouple import config as get_env
from django.conf import settings
import os

SECRET_KEY = get_env('SECRET_KEY', 'Debug')
DEBUG = get_env('DEBUG', True)

if get_env('DB_NAME', False):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_env('DB_NAME'),
            'USER': get_env('DB_USER'),
            'PASSWORD': get_env('DB_PASSWORD'),
            'HOST': get_env('DB_HOST', 'localhost'),
            'PORT': '5432',
        }
    }

settings.INSTALLED_APPS.append('corsheaders')
settings.INSTALLED_APPS.append('rest_framework')
settings.INSTALLED_APPS.append('rest_framework.authtoken')
settings.INSTALLED_APPS.append('core_app.apps.CoreAppConfig')

settings.MIDDLEWARE.append('core_app.middleware.core_middleware')
DEFAULT_APP = get_env('DEFAULT_APP', 'website_app')
DEFAULT_APP_LABEL = get_env('DEFAULT_APP_LABEL', 'Meu Projeto')
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
ALLOWED_HOSTS = ['*']
ADMINS = [('Naylson Ferreira', 'naylsonfsa@gmail.com')]
EMAIL_HOST_USER = 'naylsonfsa@gmail.com'
if get_env('EMAIL_HOST', False):
    EMAIL_HOST = get_env('EMAIL_HOST', 'localhost')
    EMAIL_HOST_PASSWORD = get_env('EMAIL_HOST_PASSWORD', '')
    EMAIL_HOST_USER = get_env('EMAIL_HOST_USER', '')
    EMAIL_PORT = get_env('EMAIL_HOST_USER', 587)
    EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'contato.overloadlab@gmail.com'
LOGIN_URL = get_env('LOGIN_URL', '/login')
LOGIN_REDIRECT_URL = '/'
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    STATICFILES_DIRS = [os.path.join(settings.BASE_DIR, "static")]
else:
    STATIC_URL = get_env('STATIC_URL', 'static/')
    STATIC_ROOT = get_env('STATIC_ROOT', 'static/')
MEDIA_URL = get_env('MEDIA_URL', 'media/')
MEDIA_ROOT = os.path.join(settings.BASE_DIR, get_env('MEDIA_ROOT', 'media/'))
FTP_STORAGE_LOCATION = get_env('FTP_STORAGE_LOCATION', False)
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    'access-control-allow-origin',
    'access-control-allow-headers',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
