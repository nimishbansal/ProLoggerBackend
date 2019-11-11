"""
WSGI config for ProLogger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProLogger.settings")
from utility.environment_utils import set_settings_module

set_settings_module()

application = get_wsgi_application()
