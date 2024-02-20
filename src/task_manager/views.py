from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from task_manager.models import Task
from task_manager.serializers import TaskSerializer


# Create your views here.
class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
