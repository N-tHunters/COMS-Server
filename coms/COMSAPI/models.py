import uuid
from django.db import models

# Create your models here.

class TASK_STATUS:
    PENDING = 0
    FINISHED = 1

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=256)
    computer = models.CharField(max_length=256)
    is_connected = models.BooleanField(default=False)


class Module(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='uploads/modules/')


class Task(models.Model):
    name = models.CharField(max_length=256)
    status = models.IntegerField(default=TASK_STATUS.PENDING)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=None)
    arguments = models.CharField(max_length=1024)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)


class Report(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    content = models.TextField()
