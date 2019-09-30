from django.urls import path, include
from .views import ProfileAPI, UserAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profileAPI', ProfileAPI)
router.register('userAPI', UserAPI)

urlpatterns = [
    path('', include(router.urls)),
]