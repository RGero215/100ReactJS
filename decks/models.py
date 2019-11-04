from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

# Create your models here.

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField(default='100react.png', upload_to='decks_pics')
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    screenshoot1 = models.ImageField(upload_to='decks_screenshots')
    screenshoot2 = models.ImageField(upload_to='decks_screenshots')
    screenshoot3 = models.ImageField(upload_to='decks_screenshots')
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('deck-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

        img = Image.open(self.icon.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.icon.path)

        screenshoot1 = Image.open(self.screenshoot1.path)
        
        if screenshoot1.height > 300 or screenshoot1.width > 300:
            output_size = (300, 300)
            screenshoot1.thumbnail(output_size)
            screenshoot1.save(self.screenshoot1.path)

        screenshoot2 = Image.open(self.screenshoot2.path)
        
        if screenshoot2.height > 300 or screenshoot2.width > 300:
            output_size = (300, 300)
            screenshoot2.thumbnail(output_size)
            screenshoot2.save(self.screenshoot2.path)

        screenshoot3 = Image.open(self.screenshoot3.path)
        
        if screenshoot3.height > 300 or screenshoot3.width > 300:
            output_size = (300, 300)
            screenshoot3.thumbnail(output_size)
            screenshoot3.save(self.screenshoot3.path)
