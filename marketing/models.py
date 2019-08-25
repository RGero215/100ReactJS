from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Groups(models.Model):
    group = models.IntegerField(default=1, unique=True)
    player_one = models.ForeignKey(User, related_name='player_one', on_delete=models.CASCADE, blank=True, null=True)
    player_two = models.ForeignKey(User, related_name='player_two', on_delete=models.CASCADE, blank=True, null=True)
    player_three = models.ForeignKey(User, related_name='player_three', on_delete=models.CASCADE, blank=True, null=True)
    player_four = models.ForeignKey(User, related_name='player_four', on_delete=models.CASCADE, blank=True, null=True)
    player_five = models.ForeignKey(User, related_name='player_five', on_delete=models.CASCADE, blank=True, null=True)
    player_six = models.ForeignKey(User, related_name='player_six', on_delete=models.CASCADE, blank=True, null=True)
    player_seven = models.ForeignKey(User, related_name='player_seven', on_delete=models.CASCADE, blank=True, null=True)
    player_eight = models.ForeignKey(User, related_name='player_eight', on_delete=models.CASCADE, blank=True, null=True)
    player_nine = models.ForeignKey(User, related_name='player_nine', on_delete=models.CASCADE, blank=True, null=True)
    player_ten = models.ForeignKey(User, related_name='player_ten', on_delete=models.CASCADE, blank=True, null=True)
    player_eleven = models.ForeignKey(User, related_name='player_elven', on_delete=models.CASCADE, blank=True, null=True)
    player_twelve = models.ForeignKey(User, related_name='player_twelve', on_delete=models.CASCADE, blank=True, null=True)
    player_thirteen = models.ForeignKey(User, related_name='player_thirteen', on_delete=models.CASCADE, blank=True, null=True)
    player_fourteen = models.ForeignKey(User, related_name='player_fourteen', on_delete=models.CASCADE, blank=True, null=True)
    player_fifteen = models.ForeignKey(User, related_name='player_fifteen', on_delete=models.CASCADE, blank=True, null=True)
    player_sixteen = models.ForeignKey(User, related_name='player_sixteen', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'Group {self.group}'

    def get_absolute_url(self):
        return reverse('marketing-home')