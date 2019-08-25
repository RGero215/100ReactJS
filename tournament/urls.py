from django.urls import path
from .views import (TournamentListView, FourPlayersCreateView, FourPlayersDetailView,
                    FourPlayersListView)

urlpatterns = [
    path('', TournamentListView.as_view(template_name='tournament/tournament.html'), name='tournament-home'),
    path('four/', FourPlayersListView.as_view(template_name='tournament/four-list.html'), name='four-list'),
    path('four/new/', FourPlayersCreateView.as_view(template_name='tournament/four-players.html'), name='four-players'),
    path('four/detail/<int:pk>/', FourPlayersDetailView.as_view(template_name='tournament/four-detail.html'), name='four-detail'),

]