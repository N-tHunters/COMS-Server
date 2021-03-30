from django.urls import path
from .views import index, computers, modules, new_module, tasks, new_task, delete_computer, delete_task, view_task

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', index, name='dashboard'),
    path('computers', computers, name='computers'),
    path('modules', modules, name='modules'),
    path('module/new', new_module, name='new_module'),
    path('tasks', tasks, name='tasks'),
    path('task/new', new_task, name='new_task'),
    path('task/delete', delete_task, name='delete_task'),
    path('computer/delete', delete_computer, name='delete_computer'),
    path('task/view/<int:id>', view_task, name='view_task')
]
