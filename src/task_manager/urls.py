from django.urls import path

from src.task_manager.apps import TaskManagerConfig
from src.task_manager.views import TaskCreateAPIView

app_name = TaskManagerConfig.name

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task_create'),
]
