"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taskmanager.views import (
    get_task_list,
    add_task, edit_task,
    toggle_task_status,
    delete_task
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_task_list, name="home"),
    path('add', add_task, name="add"),
    path('edit/<task_id>', edit_task, name="edit"),
    path('toggle/<task_id>', toggle_task_status, name="toggle"),
    path('delete/<task_id>', delete_task, name='delete')
]
