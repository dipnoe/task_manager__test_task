from django.db import models
from django.utils import timezone


class Executor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    PRIORITY = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    created = models.DateTimeField(auto_now_add=True, default=timezone.now)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=PRIORITY)
    title = models.CharField(max_length=255)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-priority', 'created']

    def __str__(self):
        return self.title
