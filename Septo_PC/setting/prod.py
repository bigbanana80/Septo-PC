from Septo_PC.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
from decouple import config

SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['septu-pc-110.ir' , 'www.septu-pc-110.ir']

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_ROOT = '/home/septupci/public_html/static'
MEDIA_ROOT = '/home/septupci/public_html/media'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

CSRF_COOKIE_SECURE = True

POSTGRES_DB = config("POSTGRES_DB") #database name
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD") # database user password
POSTGRES_USER = config("POSTGRES_USER") # database username
POSTGRES_HOST = config("POSTGRES_HOST") # database host
POSTGRES_PORT = config("POSTGRES_PORT")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
}}
