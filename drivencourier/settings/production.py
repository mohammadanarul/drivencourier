from .base import *
import django_heroku
import dj_database_url

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = ['https://driven-courier.herokuapp.com/', '*']

# database management
DATABASES = {'default': dj_database_url.config()}

django_heroku.settings(locals())

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = config('EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
