from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from src.task_manager.models import Task
from src.task_manager.serializers import TaskSerializer


# Create your views here.
class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
