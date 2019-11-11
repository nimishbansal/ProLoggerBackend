from django.conf.urls import url

from .api import views

urlpatterns = [
    url(r'^$', views.ProjectListCreateView.as_view()),
    url(r'^verify_secret_key/$', views.ProjectSecretKeyVerificationView.as_view()),
    url(r'^bulk_delete/$', views.ProjectBulkDeleteView.as_view()),
    url(r'^new_log_entry/$', views.LogEntryCreateView.as_view()),
    url(r'^(?P<project_id>[0-9]+)/log_entries/$', views.LogEntryListView.as_view()),
    url(r'^(?P<project_id>[0-9]+)/log_entries/bulk_delete/$', views.LogEntryBulkDeleteView.as_view()),
    url(r'^(?P<project_id>[0-9]+)/log_entries/(?P<pk>[0-9]+)/$', views.LogEntryRetrieveUpdateDestroyView.as_view()),
    url(r'^sample/$', views.sample),
]

