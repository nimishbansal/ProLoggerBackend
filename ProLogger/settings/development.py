from .base import *
from utility.environment_utils import DEVELOPMENT
import random


ENVIRONMENT = DEVELOPMENT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prologger',
        'USER': 'django',
        'PASSWORD': '123456',
        'HOST': '0.0.0.0',  # Or an IP Address that your DB is hosted on
        'PORT': '',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
    }
}


MEDIA_URL = '/media/'
