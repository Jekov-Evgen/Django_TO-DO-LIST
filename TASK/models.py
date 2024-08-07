from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    name_task = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_task = models.IntegerField(default=0)

    def __str__(self):
        return self.name_task
