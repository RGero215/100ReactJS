from django.urls import path
from .views import (Test100ReactListView, Test100ReactDetailView, 
                    Test100ReactCreate, Test100ReactPlayCreate, 
                    Test100ReactPlayDetailView, PlayerListView)


urlpatterns = [
    path('', Test100ReactCreate.as_view(template_name='test100react/test-create.html'), name='test-create'),
    path('test/', Test100ReactListView.as_view(template_name='test100react/test.html'), name='test-test'),
    path('test/<int:pk>/', Test100ReactDetailView.as_view(template_name='test100react/test-detail.html'), name='test-detail'),
    path('test/<int:away>/play/', Test100ReactPlayCreate.as_view(template_name='test100react/test-play.html'), name='test-play'),
    path('test/<int:away>/play/<int:pk>/', Test100ReactPlayDetailView.as_view(template_name='test100react/play-detail.html'), name='play-detail'),
    path('test/player/<str:player>', PlayerListView.as_view(template_name='test100react/player-list.html'), name='player-list'),
]