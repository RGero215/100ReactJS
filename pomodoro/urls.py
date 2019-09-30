from django.urls import path, include
from .views import (PomodoroListView, PomodoroDetailView, PomodoroCreateView,
            PomodoroUpdateView, PomodoroGroupCreateView, PomodoroSingleUpdateView, PomodoroAPI)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pomodoroAPI', PomodoroAPI)

urlpatterns = [
    path('', PomodoroListView.as_view(template_name='pomodoro/pomodoros.html'),name='pomodoros-home'),
    path('api/', include(router.urls)),
    path('new/', PomodoroCreateView.as_view(template_name='pomodoro/new.html'), name='pomodoro-new'),
    path('new/single/<int:pk>/', PomodoroSingleUpdateView.as_view(template_name='pomodoro/play.html'), name='single-play'),
    path('new/<int:challenge>/', PomodoroGroupCreateView.as_view(template_name='pomodoro/newgroup.html'), name='pomodoro-newgroup'),
    path('new/<int:challenge>/<int:pk>/', PomodoroUpdateView.as_view(template_name='pomodoro/play.html'), name='pomodoro-play'),
    path('<int:pk>/', PomodoroDetailView.as_view(template_name='pomodoro/detail.html'), name='pomodoro-detail')
]