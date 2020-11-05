from django.urls import path
from .views import index, computers

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', index, name='dashboard'),
    path('computers', computers, name='computers')
]
