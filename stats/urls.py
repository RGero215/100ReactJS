from django.urls import path
from .views import (StatsListView, StatsDetailView, 
                    UserStatsListView, StatsCreateView, 
                    PlayCardCreateView, PlayCardDetailView,
                    TwoGamesCreateView, TwoGamesDetailView)


urlpatterns = [
    path('', StatsListView.as_view(template_name='stats/stats.html'), name='stats-home'),
    path('play/two/<int:pk>/', TwoGamesCreateView.as_view(template_name='stats/play-two.html'), name='play-two'),
    path('play/', StatsCreateView.as_view(template_name='stats/play.html'), name='stat-play'),
    path('play/two-card/<int:pk>/', TwoGamesDetailView.as_view(template_name='stats/two-games-card.html'), name='two-games-card'),
    path('play/<int:away>/play', PlayCardCreateView.as_view(template_name='stats/play-card.html'), name='play-card'),
    path('play/<int:away>/play/<int:pk>/', PlayCardDetailView.as_view(template_name='stats/compare-card.html'), name='compare-card'),
    path('<str:username>/', UserStatsListView.as_view(template_name='stats/user-stats.html'), name='user-stats'),
    path('stat/<int:pk>/', StatsDetailView.as_view(template_name='stats/stat-detail.html'), name='stat-detail'),
]