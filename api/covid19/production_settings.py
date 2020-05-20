import os

from covid19.settings import BASE_DIR
from covid19.settings import *

ALLOWED_HOSTS = ["*"]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CORS_ORIGIN_WHITELIST = (
    os.environ.get('FRONETEND_HOST', default=""),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'covid19',
        'USER': os.environ.get('DB_USERNAME', default=""),
        'PASSWORD': os.environ.get('DB_PASSWORD', default=""),
        'HOST': os.environ.get('DB_HOST', default=""),
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO,ONLY_FULL_GROUP_BY',
        }
    }
}
