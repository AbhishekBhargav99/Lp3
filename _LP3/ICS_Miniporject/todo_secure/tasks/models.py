from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length = 30)
    complete = models.BooleanField(default = False)
