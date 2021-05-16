from .base import *
import os


LOCAL_DB = {
    'NAME' : os.getenv('LOCAL_NAME'),
    'USER' : os.getenv('LOCAL_USER'),
    'PASSWORD' : os.getenv('LOCAL_PASSWORD'),
    'HOST' : os.getenv('LOCAL_HOST'),
    'PORT' : os.getenv('LOCAL_PORT'),
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        **LOCAL_DB
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_5=#=+cl&lp@&ayps6ia0viff)^v$_wvutyyxca!xu0w6d2z3$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]