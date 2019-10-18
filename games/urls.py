from django.urls import path, include
from .views import GameAPI
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "100React API"
router.register('gameAPI', GameAPI)

urlpatterns = [
    path('api/', include(router.urls)),
]