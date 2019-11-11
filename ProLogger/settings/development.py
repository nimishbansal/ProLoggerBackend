from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prologger',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '0.0.0.0',  # Or an IP Address that your DB is hosted on
        'PORT': '',
        'OPTIONS': {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
        },
    }
}
