# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import TaskItem


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def task_list_view(request):
    tasks = TaskItem.objects.filter(user_pk=request.user.pk)
    if request.method == "POST":
        data = request.POST
        if action != None: #data.get("action") = "add"
            TaskItem.objects.create(user_pk=request.user.pk, index=len(tasks) + 1, description=data.get("description"), complete=False)
        else: #deleting item
            TaskItem.objects.filter(user_pk=request.user.pk, index=data.get(int("delete_index")))
        return render(request, "task_list.html",TaskItem.objects.filter(user_pk=request.user.pk))
    context = {'task_list':tasks}
    return render(request, "task_list.html",context)