from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Test100React(models.Model):
    player = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(default='account.png', upload_to='test100react_pics')
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
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.email}'

    def get_absolute_url(self):
        return reverse('test-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)