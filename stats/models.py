from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from tournament.models import Four

# Create your models here.
class Statistics(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    opponent = models.ForeignKey(User, related_name='opponent', default=None, null=True, on_delete=models.CASCADE)
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
    result = models.CharField(max_length=100, blank=True, null=True, default=None)
    winnings = models.CharField(max_length=100, blank=True, null=True, default=None)
    home = models.IntegerField(default=0)
    away = models.IntegerField(default=0)
    image = models.ImageField(default='100React.png', upload_to='stats_pics')
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.player.username}'

    def get_absolute_url(self):
        return reverse('stats-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class OnePLayer(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='account.png', upload_to='one_player_pics')
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
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.player}'

    def get_absolute_url(self):
        return reverse('test-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class TwoGames(models.Model):
    four = models.ForeignKey(Four, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='account.png', upload_to='one_player_pics')
    firstAtBats = models.IntegerField(default=0)
    firstAvg = models.IntegerField(default=0)
    firstDoubles = models.IntegerField(default=0)
    firstHits = models.IntegerField(default=0)
    firstHomeRuns = models.IntegerField(default=0)
    firstLob = models.IntegerField(default=0)
    firstPoints = models.IntegerField(default=0)
    firstRbi = models.IntegerField(default=0)
    firstRuns = models.IntegerField(default=0)
    firstSingles = models.IntegerField(default=0)
    firstSlg = models.IntegerField(default=0)
    firstTriples = models.IntegerField(default=0)
    firstResult = models.CharField(max_length=1, blank=True, null=True, default=None)
    firstHome = models.IntegerField(default=0)
    firstAway = models.IntegerField(default=0)
    firstRisk = models.IntegerField(default=0)
    firstSafe = models.IntegerField(default=0)
    firstGrandSlam = models.IntegerField(default=0)
    firstOff = models.IntegerField(default=0)
    firstStop = models.IntegerField(default=0)
    firstLevel = models.CharField(max_length=20, blank=True, null=True, default='Rookie')
    firstFinal = models.BooleanField(default=False)
    secondAtBats = models.IntegerField(default=0)
    secondAvg = models.IntegerField(default=0)
    secondDoubles = models.IntegerField(default=0)
    secondHits = models.IntegerField(default=0)
    secondHomeRuns = models.IntegerField(default=0)
    secondLob = models.IntegerField(default=0)
    secondPoints = models.IntegerField(default=0)
    secondRbi = models.IntegerField(default=0)
    secondRuns = models.IntegerField(default=0)
    secondSingles = models.IntegerField(default=0)
    secondSlg = models.IntegerField(default=0)
    secondTriples = models.IntegerField(default=0)
    secondResult = models.CharField(max_length=1, blank=True, null=True, default=None)
    secondHome = models.IntegerField(default=0)
    secondAway = models.IntegerField(default=0)
    secondRisk = models.IntegerField(default=0)
    secondSafe = models.IntegerField(default=0)
    secondGrandSlam = models.IntegerField(default=0)
    secondOff = models.IntegerField(default=0)
    secondStop = models.IntegerField(default=0)
    secondLevel = models.CharField(max_length=20, blank=True, null=True, default='Rookie')
    secondFinal = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.player}'

    def get_absolute_url(self):
        return reverse('test-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)