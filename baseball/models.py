from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from games.models import Game

# Create your models here.
class Baseball(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='account.png', upload_to='pomodoro_pics')
    atBats = models.IntegerField(default=0)
    avg = models.IntegerField(default=0)
    doubles = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    homeRuns = models.IntegerField(default=0)
    lob = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    singles = models.IntegerField(default=0)
    slg = models.IntegerField(default=0)
    triples = models.IntegerField(default=0)
    result = models.CharField(max_length=1, blank=True, null=True, default=None)
    home = models.IntegerField(default=0)
    away = models.IntegerField(default=0)
    grandSlam = models.IntegerField(default=0)
    risk = models.IntegerField(default=0)
    safe = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)
    level = models.CharField(max_length=20, blank=True, null=True, default='Rookie')
    final = models.BooleanField(default=False)
    firstHome = models.IntegerField(default=0)
    firstPoints = models.IntegerField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)