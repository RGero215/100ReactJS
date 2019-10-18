from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Baseball
from rest_framework import viewsets
from .serializers import BaseballSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# Create your views here.

class BaseballAPI(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Baseball.objects.all()
    serializer_class = BaseballSerializer
