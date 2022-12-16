from .base import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%pj!a&951ecnhd69@-%$6rn+t38oo3h21=))9t=$@f401)vp#+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Permite crear una lista para indicar que IP's se pueden conectar a nuestro aplicativo.
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_app_pokemon',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',  #localhost, '127.0.0.1'
        'PORT': '5432'   #5432
    }
}

"""
-> Base de Datos relacionales:
 - mysql
 - postgresql
 - sqlserver
 - RDS (AWS)
-> Base de Datos no relaciones:
- firebase
- mongo DB
- Dynamo DB (AWS)
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = [
    BASE_DIR / 'static',  # noqa: F405
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405


