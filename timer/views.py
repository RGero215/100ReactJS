from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Timer
from rest_framework import viewsets
from .serializers import TimerSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# Create your views here.

class TimerAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
