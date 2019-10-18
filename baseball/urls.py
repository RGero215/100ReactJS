from django.urls import path, include
from .views import BaseballAPI
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "100React API"
router.register('baseballAPI', BaseballAPI)

urlpatterns = [
    path('api/', include(router.urls)),
]