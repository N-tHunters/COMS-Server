from django.db import models

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=256)
    computer = models.CharField(max_length=256)
    is_connected = models.BooleanField(default=False)

