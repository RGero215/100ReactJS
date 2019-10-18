from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from games.models import Game

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

