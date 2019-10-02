from django.urls import path, include
from .views import ProfileAPI, UserAPI, LoginAPI, UserRegisterAPI
from rest_framework import routers


router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "100React API"
router.register('profileAPI', ProfileAPI, base_name='profile')
router.register('userAPI', UserAPI, base_name='user')
# router.register('loginAPI', LoginAPI, base_name='login')
router.register('userRegisterAPI', UserRegisterAPI, base_name='register')

urlpatterns = [
    path('', include(router.urls)),
    path('loginAPI/', LoginAPI.as_view(), name="login"),
]