import os

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include

from utility.environment_utils import DEVELOPMENT


def home(index):
    return HttpResponse(str(os.environ.get('ENVIRONMENT')))


urlpatterns = [
    url(r'^$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('Project.urls')),
    url(r'^auth/', include('Auth.urls')),
]

if (settings.DEBUG and settings.ENVIRONMENT == DEVELOPMENT) or True:  # remove true later
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
