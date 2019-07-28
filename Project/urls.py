from django.conf.urls import url

from .api import views

urlpatterns = [
    url(r'(?P<project_id>[0-9]+)/log_entries/$', views.LogEntryListView.as_view()),
    url(r'(?P<project_id>[0-9]+)/log_entries/(?P<pk>[0-9]+)/$', views.LogEntryRetrieveUpdateDestroyView.as_view()),
]
