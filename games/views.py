from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Game
from rest_framework import viewsets
from .serializers import GameSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
# Create your views here.

class GameAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
