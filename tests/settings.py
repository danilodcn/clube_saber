import factory

from explorer2go.settings import *  # noqa

factory.Faker._DEFAULT_LOCALE = 'pt_BR'


SECRET_KEY = 'test_secret_key'

AWS_ACCESS_KEY_ID = 'test_aws_access_key'
AWS_SECRET_ACCESS_KEY = 'test_aws_secret_key'

STATICFILES_LOCATION = os.path.join(BASE_DIR, 'tests/static')   # noqa
MEDIA_LOCATION = os.path.join(BASE_DIR, 'tests/media')   # noqa

STORAGES['default'] = {  # type: ignore # noqa
    'BACKEND': 'django.core.files.storage.FileSystemStorage',
    'OPTIONS': {
        'location': MEDIA_LOCATION,
        'base_url': '/media/',
    },
}

STORAGES['staticfiles'] = {  # type: ignore # noqa
    'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    'OPTIONS': {
        'location': STATICFILES_LOCATION,
        'base_url': '/static/',
    },
}
