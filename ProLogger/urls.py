from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('Project.urls')),
    url(r'^auth/', include('Auth.urls')),
]
