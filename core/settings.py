"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os,ast
from dotenv import load_dotenv
from import_export.formats.base_formats import CSV,XLSX
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^$#3@3)yfa!!)5y+ss_dop*01fn=&t=cjnwwshw(*8$#6k12_9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_gis",
    "corsheaders",
    "accounts",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "djoser",
    "Data_Analyst",
    "import_export",
    "django.contrib.gis",
    "django_filters",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'postgres', 
#         'USER': 'postgres',
#         'PASSWORD': 'hello',
#         'HOST': '127.0.0.1', 
#         'PORT': '5432',
#     }
# }


# render
DATABASES = {
    'default':{
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': "deportal_db_user",
        'PASSWORD': "Rel8G9kqNIgwFQAJV0PcSerh1fmBdTmZ",
        'HOST': "dpg-cm55u6un7f5s73c34410-a.singapore-postgres.render.com",
        'NAME':"deportal_db",
    }
}

# Vercel
# DATABASES = {
#     'default':{
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'USER': "default",
#         'PASSWORD': "4jKDRPgucN1V",
#         'HOST': "ep-wild-meadow-83018427-pooler.ap-southeast-1.postgres.vercel-storage.com",
#         'NAME':"verceldb",
#     }
# }


## EMAIL SETTINGS
## EMAIL SETTINGS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "pukh.raj@inverv.com"
EMAIL_HOST_PASSWORD = 'roqw pzyn hkqe tjip'
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = os.environ["SENDER_EMAIL"]
# ADMINS_EMAIL = os.environ["ADMINS_EMAIL"]



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

## REST_FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    
}

## JWT AUTHORIZATION
SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

##DJOSER SETTINGS
DJOSER = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'LOGIN_FIELD':'email',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'SET_PASSWORD_RETYPE':True,
    'SET_USERNAME_RETYPE':True,
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL':'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':False,
    'SERIALIZERS':{
        'user_create':'accounts.serializers.UserCreateSerializer',
        'user':'accounts.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializer.UserDeleteSerializer'
    },
}

AUTH_USER_MODEL = 'accounts.userAccount'


## IMPORT_EXPORT SETTINGS
IMPORT_EXPORT_FORMATS = [XLSX,CSV]
IMPORT_FORMATS =[CSV,XLSX]
EXPORT_FORMATS =[CSV,XLSX]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

## CSRF SETTINGS

CORS_ALLOW_ALL_ORIGINS=True

# CSRF_TRUSTED_ORIGINS = [
#     "http://127.0.0.1:8000/",
# ]

CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]




GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal308.dll'