from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


TypeOfGames = (('1','Focus'), ('2','Memory'),('3','Reaction Time'))
    

class Game(models.Model):
    name = models.CharField(max_length=25)
    game_type = models.CharField(max_length=25,choices=TypeOfGames)# Choices is a list of Tuple)  #(focus, memory, etc.)
    average_score = models.IntegerField(default=0)#Int (avg. score across all users who complete the game)
    win_rate = models.IntegerField(default=0)#Int (% of users who win)