import os

PRODUCTION = 'production'
TESTING = 'testing'
DEVELOPMENT = 'development'


def set_settings_module():
    if os.environ.get('ENVIRONMENT') == PRODUCTION:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProLogger.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProLogger.settings.development')
