# accounts/urls.py
#from django.urls import path
from django.conf.urls import url
from .views import SignUpView, task_list_view


urlpatterns = [
    url(r"^signup/", SignUpView.as_view(), name="signup"),
	url(r"^tasks/", task_list_view),
]