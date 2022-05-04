# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import TaskItem
from django.shortcuts import render


def task_list_view(request):
    tasks = TaskItem.objects.filter(user_pk=request.user.pk)
    if request.method == "POST":
        data = request.POST
        if data.get("action") == "add": #data.get("action") = "add"
            TaskItem.objects.create(user_pk=request.user.pk, index=len(tasks) + 1, description=data.get("description"), complete=False)
        else: #deleting item
            TaskItem.objects.get(id=int(data.get("delete_index"))).delete()
        context = {'task_list':TaskItem.objects.filter(user_pk=request.user.pk)}
    else:
        context = {'task_list':TaskItem.objects.filter(user_pk=request.user.pk), 'fade_in': True}
    return render(request, "task_list.html",context)    
	
	