from django.shortcuts import render, HttpResponse


# Create your views here.
def get_task_list(request):
    return render(request, 'taskmanager/todo_list.html')
