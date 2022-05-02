# accounts/urls.py
#from django.urls import path
from django.conf.urls import url
from .views import SignUpView


urlpatterns = [
    path(r"^signup/", SignUpView.as_view(), name="signup"),
]