from Septo_PC.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a&&a*^%#1zuv-8=3-+$(oe76@inmm_&qr8zox2x^17*k0%=6k1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = []
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_ROOT = BASE_DIR / "media"

CSRF_COOKIE_SECURE = True