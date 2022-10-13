from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
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


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = TaskForm(instance=task)
    context = {"form": form}
    return render(request, "taskmanager/edit_task.html", context)


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
