from django.contrib import admin

from task_manager.models import Task, Executor


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.get_fields()]


@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ['name',]
