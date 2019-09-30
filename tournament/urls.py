from django.urls import path, include
from .views import (TournamentListView, FourPlayersCreateView, FourPlayersDetailView,
                    FourPlayersListView, FourPomodoroCreateView, FourPomodoroDetailView,
                    FourPomodoroListView, FourPlayersAPI, FourPomodoroAPI)

from rest_framework import routers

router = routers.DefaultRouter()
router.register('fourPlayersAPI', FourPlayersAPI)
router.register('fourPomodoroAPI', FourPomodoroAPI)

app_name = 'tournament'
urlpatterns = [
    path('', TournamentListView.as_view(template_name='tournament/tournament.html'), name='tournament-home'),
    path('api/', include((router.urls, app_name))),
    path('four/', FourPlayersListView.as_view(template_name='tournament/four-list.html'), name='four-list'),
    path('four/new/', FourPlayersCreateView.as_view(template_name='tournament/four-players.html'), name='four-players'),
    path('four/detail/<int:pk>/', FourPlayersDetailView.as_view(template_name='tournament/four-detail.html'), name='four-detail'),
    path('four/pomodoro/', FourPomodoroListView.as_view(template_name='tournament/pomodoro-list.html'), name='pomodoro-list'),
    path('four/pomodoro/new/', FourPomodoroCreateView.as_view(template_name='tournament/pomodoro-players.html'), name='pomodoro-players'),
    path('four/pomodoro/detail/<int:pk>/', FourPomodoroDetailView.as_view(template_name='tournament/pomodoro-detail.html'), name='pomodoro-detail'),

]