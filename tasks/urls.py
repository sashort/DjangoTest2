# accounts/urls.py
#from django.urls import path
from django.conf.urls import url
from .views import SignUpView, task_list_view


urlpatterns = [
    url('', task_list_view, name="task list"),
]