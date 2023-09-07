import os
from pathlib import Path

import environ
import sentry_sdk
from django.utils.translation import gettext_lazy as _
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = env('SECRET_KEY', default='secret_key')  # type: ignore

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

SHARED_APPS = [
    'django_tenants',
    'explorer2go.apps.tenant',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'colorfield',
    'import_export',
    'fontawesomefree',
]

SHOW_PUBLIC_IF_NO_TENANT_FOUND = True

TENANT_APPS = [
    'explorer2go.apps.web',
    'explorer2go.apps.product',
]

TENANT_MODEL = 'tenant.Tenant'
TENANT_DOMAIN_MODEL = 'tenant.Domain'

INSTALLED_APPS = SHARED_APPS + TENANT_APPS

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'explorer2go.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['explorer2go/templates'],
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

SENTRY_DNS: str = env('SENTRY_DNS', default='')  # type: ignore

if SENTRY_DNS:
    sentry_sdk.init(
        dsn=SENTRY_DNS,
        integrations=[DjangoIntegration()],
        send_default_pii=True,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='bucket')  # type: ignore # noqa

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='aws_access_key')  # type: ignore # noqa
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='aws_secret_key')  # type: ignore # noqa

AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', default='')  # type: ignore # noqa

STATICFILES_LOCATION = 'static'
STORAGES = {
    'default': {'BACKEND': 'explorer2go.apps.tenant.storage.TenantS3Storage'},
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3StaticStorage',
        'OPTIONS': {
            'location': STATICFILES_LOCATION,
        },
    },
}

if DEBUG:
    MEDIA_ROOT = 'media/'
    MEDIA_URL = '/media/'
    STORAGES['default'] = {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
        'OPTIONS': {
            'location': 'media',
            'base_url': '/media/',
        },
    }

WSGI_APPLICATION = 'explorer2go.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': env.db(default='sqlite:///:memory:'),  # type: ignore
}

DATABASES['default']['ENGINE'] = 'django_tenants.postgresql_backend'

DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


LANGUAGES = (
    ('en-us', _('English')),
    ('pt-br', _('Portuguese Brazil')),
)

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_TRUSTED_ORIGINS = [
    'https://clubesaber.com/',
    'https://*.clubesaber.com/',
    'https://clubesaber.com/',
    'https://*.clubesaber.store/',
    'http://*.clubesaber.store/',
]
