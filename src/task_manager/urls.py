from django.urls import path

from task_manager.apps import TaskManagerConfig
from task_manager.views import TaskCreateAPIView, TaskUpdateAPIView, TaskDestroyAPIView

app_name = TaskManagerConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task_update'),
    path('destroy/<int:pk>/', TaskDestroyAPIView.as_view(), name='task_destroy'),
]
