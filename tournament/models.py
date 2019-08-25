from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# class Two(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     player_one = models.ForeignKey(TwoGames, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(TwoGames, related_name='player_two', on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(default=timezone.now)
#     ended = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.player_one.player} vs {self.player_two.player}'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})


class Four(models.Model):
    player_one = models.ForeignKey(User, on_delete=models.CASCADE)
    player_two = models.ForeignKey(User, related_name='four_player_two', on_delete=models.CASCADE)
    player_three = models.ForeignKey(User, related_name='four_player_three', on_delete=models.CASCADE)
    player_four = models.ForeignKey(User, related_name='four_player_four', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    ended = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.player_one} vs {self.player_two} | {self.player_three} vs {self.player_four}'

    def get_absolute_url(self):
        return reverse('stats-detail', kwargs={'pk': self.pk})

# class Six(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='six_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='six_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='six_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='six_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='six_player_six', on_delete=models.CASCADE)


#     def __str__(self):
#         return 'Six Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})

# class Eight(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='eight_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='eight_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='eight_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='eight_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='eight_player_six', on_delete=models.CASCADE)
#     player_seven = models.ForeignKey(Statistics, related_name='eight_player_seven', on_delete=models.CASCADE)
#     player_eight = models.ForeignKey(Statistics, related_name='eight_player_eight', on_delete=models.CASCADE)


#     def __str__(self):
#         return 'Eight Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})

# class Ten(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='ten_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='ten_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='ten_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='ten_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='ten_player_six', on_delete=models.CASCADE)
#     player_seven = models.ForeignKey(Statistics, related_name='ten_player_seven', on_delete=models.CASCADE)
#     player_eight = models.ForeignKey(Statistics, related_name='ten_player_eight', on_delete=models.CASCADE)
#     player_nine = models.ForeignKey(Statistics, related_name='ten_player_nine', on_delete=models.CASCADE)
#     player_ten = models.ForeignKey(Statistics, related_name='ten_player_ten', on_delete=models.CASCADE)



#     def __str__(self):
#         return 'Ten Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})

# class Twelve(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='twelve_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='twelve_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='twelve_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='twelve_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='twelve_player_six', on_delete=models.CASCADE)
#     player_seven = models.ForeignKey(Statistics, related_name='twelve_player_seven', on_delete=models.CASCADE)
#     player_eight = models.ForeignKey(Statistics, related_name='twelve_player_eight', on_delete=models.CASCADE)
#     player_nine = models.ForeignKey(Statistics, related_name='twelve_player_nine', on_delete=models.CASCADE)
#     player_ten = models.ForeignKey(Statistics, related_name='twelve_player_ten', on_delete=models.CASCADE)
#     player_eleven = models.ForeignKey(Statistics, related_name='twelve_player_elven', on_delete=models.CASCADE)
#     player_twelve = models.ForeignKey(Statistics, related_name='twelve_player_twelve', on_delete=models.CASCADE)



#     def __str__(self):
#         return 'Twelve Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})

# class Fourteen(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='fourteen_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='fourteen_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='fourteen_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='fourteen_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='fourteen_player_six', on_delete=models.CASCADE)
#     player_seven = models.ForeignKey(Statistics, related_name='fourteen_player_seven', on_delete=models.CASCADE)
#     player_eight = models.ForeignKey(Statistics, related_name='fourteen_player_eight', on_delete=models.CASCADE)
#     player_nine = models.ForeignKey(Statistics, related_name='fourteen_player_nine', on_delete=models.CASCADE)
#     player_ten = models.ForeignKey(Statistics, related_name='fourteen_player_ten', on_delete=models.CASCADE)
#     player_eleven = models.ForeignKey(Statistics, related_name='fourteen_player_elven', on_delete=models.CASCADE)
#     player_twelve = models.ForeignKey(Statistics, related_name='fourteen_player_twelve', on_delete=models.CASCADE)
#     player_thirteen = models.ForeignKey(Statistics, related_name='fourteen_player_thirteen', on_delete=models.CASCADE)
#     player_fourteen = models.ForeignKey(Statistics, related_name='fourteen_player_fourteen', on_delete=models.CASCADE)



#     def __str__(self):
#         return 'Fourteen Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})
        

# class Sixteen(models.Model):
#     player_one = models.ForeignKey(Statistics, on_delete=models.CASCADE)
#     player_two = models.ForeignKey(Statistics, related_name='sixteen_player_two', on_delete=models.CASCADE)
#     player_three = models.ForeignKey(Statistics, related_name='sixteen_player_three', on_delete=models.CASCADE)
#     player_four = models.ForeignKey(Statistics, related_name='sixteen_player_four', on_delete=models.CASCADE)
#     player_five = models.ForeignKey(Statistics, related_name='sixteen_player_five', on_delete=models.CASCADE)
#     player_six = models.ForeignKey(Statistics, related_name='sixteen_player_six', on_delete=models.CASCADE)
#     player_seven = models.ForeignKey(Statistics, related_name='sixteen_player_seven', on_delete=models.CASCADE)
#     player_eight = models.ForeignKey(Statistics, related_name='sixteen_player_eight', on_delete=models.CASCADE)
#     player_nine = models.ForeignKey(Statistics, related_name='sixteen_player_nine', on_delete=models.CASCADE)
#     player_ten = models.ForeignKey(Statistics, related_name='sixteen_player_ten', on_delete=models.CASCADE)
#     player_eleven = models.ForeignKey(Statistics, related_name='sixteen_player_elven', on_delete=models.CASCADE)
#     player_twelve = models.ForeignKey(Statistics, related_name='sixteen_player_twelve', on_delete=models.CASCADE)
#     player_thirteen = models.ForeignKey(Statistics, related_name='sixteen_player_thirteen', on_delete=models.CASCADE)
#     player_fourteen = models.ForeignKey(Statistics, related_name='sixteen_player_fourteen', on_delete=models.CASCADE)
#     player_fifteen = models.ForeignKey(Statistics, related_name='sixteen_player_fifteen', on_delete=models.CASCADE)
#     player_sixteen = models.ForeignKey(Statistics, related_name='sixteen_player_sixteen', on_delete=models.CASCADE)



#     def __str__(self):
#         return 'Sixteen Players Tournament'

#     def get_absolute_url(self):
#         return reverse('stats-detail', kwargs={'pk': self.pk})