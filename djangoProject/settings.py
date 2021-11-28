import dotenv
import os.path
import storages.backends.s3boto3

from pathlib import Path
from os import getenv, path
from decouple import config
from django.core.management.utils import get_random_secret_key


BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_file = os.path.join(BASE_DIR, ".env")
dotenv.load_dotenv(dotenv_file)

SECRET_KEY = get_random_secret_key()

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'movies.apps.MoviesConfig',
    'crispy_forms',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
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

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'djangoProject.wsgi.application'

FILTERS_EMPTY_CHOICE_LABEL = None


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("RDS_NAME"),
        'USER': config("RDS_USER"),
        'PASSWORD': config("RDS_PASSWORD"),
        'HOST': config("HOST"),
        'PORT': config("PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles/media')
# MEDIA_URL = '/staticfiles/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'movies-home'
LOGIN_URL = 'login'

DEBUG = config("DEBUG") == "TRUE"

if DEBUG:

    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
      BASE_DIR / "static"
    ]

else:
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_REGION_NAME = config("AWS_REGION_NAME")
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
