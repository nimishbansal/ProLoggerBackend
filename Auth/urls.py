from django.conf.urls import url

from .api import views

urlpatterns = [
    url(r'send_otp/', views.send_otp),
    url(r'verify_otp/', views.verify_otp),
]
