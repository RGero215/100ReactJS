from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from tasks.models import Task
from games.models import Game

# Create your models here.
class Timer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    time_left = models.IntegerField(default=25)
