from django.shortcuts import render, HttpResponse, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def get_task_list(request):
    tasks = Task.objects.all()
    return render(request, 'taskmanager/todo_list.html', {"items": tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = TaskForm()
    context = {"form": form}
    return render(request, "taskmanager/add_task.html", context)
