from django.urls import path, include
from .views import HomePage
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groupsAPI', views.GroupAPI)


urlpatterns = [
    path('', HomePage.as_view(template_name='marketing/home.html'), name='marketing-home'),
    path('api/', include(router.urls))
    
]