from .base import *
from utility.environment_utils import PRODUCTION

print("in production")
DEBUG = False
ENVIRONMENT = PRODUCTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prologger',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dev"),
)
