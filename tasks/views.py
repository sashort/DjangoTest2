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
        if data.get("action") != None: #data.get("action") = "add"
            TaskItem.objects.create(user_pk=request.user.pk, index=len(tasks) + 1, description=data.get("description"), complete=False)
        else: #deleting item
            print("Attempting to remove: " + data.get("delete_index")
            TaskItem.objects.filter(user_pk=request.user.pk, index=data.get(int(data.get("delete_index"))))
    context = {'task_list':TaskItem.objects.filter(user_pk=request.user.pk)}
    return render(request, "task_list.html",context)
	
	