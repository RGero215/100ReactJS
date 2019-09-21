from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from stats.models import OnePLayer
from tournament.models import FourPomodoro


# Create your models here.
class Pomodoro(models.Model):
    four = models.ForeignKey(FourPomodoro, on_delete=models.CASCADE, blank=True, null=True)
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
    risk = models.IntegerField(default=0)
    safe = models.IntegerField(default=0)
    grandSlam = models.IntegerField(default=0)
    off = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)
    level = models.CharField(max_length=20, blank=True, null=True, default='Rookie')
    final = models.BooleanField(default=False)
    title = models.CharField(max_length=250)
    task_one = models.CharField(max_length=250)
    task_two = models.CharField(max_length=250)
    task_three = models.CharField(max_length=250)
    task_four = models.CharField(max_length=250)
    work_duration = models.IntegerField(default=0)
    break_duration = models.IntegerField(default=0)
    workTotal = models.CharField(max_length=10, blank=True, null=True, default=None)
    breakTotal = models.CharField(max_length=10, blank=True, null=True, default=None)
    donation = models.IntegerField(default=0)
    firstHome = models.IntegerField(default=0)
    firstPoints = models.IntegerField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.player}'

    def get_absolute_url(self):
        return reverse('pomodoro-detail', kwargs={'pk': self.pk})

