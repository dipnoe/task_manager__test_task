from rest_framework.viewsets import ModelViewSet

from task_manager.models import Task
from task_manager.serializers import TaskSerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
