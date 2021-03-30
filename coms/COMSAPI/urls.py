from django.urls import path

from . import views

urlpatterns = [
    path('client/', views.ClientView.as_view()),
    path('task/', views.TaskView.as_view()),
    path('report/', views.ReportView.as_view()),
    path('connect', views.connect_client),
    path('disconnect', views.connect_client)
]
