from django.urls import path
from .views import index, computers, modules, new_module, tasks, new_task

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', index, name='dashboard'),
    path('computers', computers, name='computers'),
    path('modules', modules, name='modules'),
    path('module/new', new_module, name='new_module'),
    path('tasks', tasks, name='tasks'),
    path('task/new', new_task, name='new_task')
]
