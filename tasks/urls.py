from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.create_task, name='create_task'),
    path('list/', views.task_list, name='task_list'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('pendingtask/', views.pending_task, name='pending_task'),
    path('completedtask/', views.completed_task, name='completed_task'),
    path('donetask/<int:task_id>/', views.done_task, name='done_task'),
]