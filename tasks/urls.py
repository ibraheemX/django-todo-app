from django.urls import path
from .import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('delete/<int:task_id>/', views.delete_task,name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task,name='edit_task')
]
