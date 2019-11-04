from django.urls import path, include
from .views import (DeckCreateView, DeckAPI, DeckListView, DeckDetailView, 
                    DeckDeleteView, DeckUpdateView)

from rest_framework import routers

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "100React API"
router.register('deckAPI', DeckAPI)

urlpatterns = [
    path('api/', include(router.urls)),
    path('user/<str:username>/', DeckListView.as_view(), name='user-posts'),
    path('<int:pk>/', DeckDetailView.as_view(), name='deck-detail'),
    path('new/', DeckCreateView.as_view(template_name='decks/new.html'), name='deck-new'),
    path('<int:pk>/update/', DeckUpdateView.as_view(), name='deck-update'),
    path('<int:pk>/delete/', DeckDeleteView.as_view(), name='deck-delete'),
]