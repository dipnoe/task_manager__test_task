from django.urls import path

from task_manager.apps import TaskManagerConfig
from task_manager.views import TaskViewSet

app_name = TaskManagerConfig.name

urlpatterns = [
    path('create/', TaskViewSet.as_view({
        'post': 'create'
    }), name='task_create'),
    path('update/<int:pk>/', TaskViewSet.as_view({
        'patch': 'update'
    }), name='task_update'
         ),
    path('destroy/<int:pk>/', TaskViewSet.as_view({
        'delete': 'destroy'
    }), name='task_destroy'
    ),
    path('list/', TaskViewSet.as_view({
        'get': 'list'
    }), name='task_list'),
]
