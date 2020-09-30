from .base import *
from utility.environment_utils import PRODUCTION

print("in production")
DEBUG = True
# DEBUG = False
ENVIRONMENT = PRODUCTION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prologger',
        'USER': 'root',
        'PASSWORD': 'abcd1234',
        'HOST': 'prologger.chje1lmkdc3f.us-east-1.rds.amazonaws.com',  # Or an IP Address that your DB is hosted on
        'PORT': '5432',
        # 'OPTIONS': {
        #     # Tell MySQLdb to connect with 'utf8mb4' character set
        #     'charset': 'utf8mb4',
        # },
    }
}

# STATICFILES_DIRS = (
    # os.path.join('/home/ubuntu/', "static_dev"),
    # os.path.join(BASE_DIR, "static_dev"),
# )

YOUR_S3_BUCKET = "static-files-for-zappa"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = YOUR_S3_BUCKET

# These next two lines will serve the static files directly
# from the s3 bucket
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % YOUR_S3_BUCKET
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN



MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
