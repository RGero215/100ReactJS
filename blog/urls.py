from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostAPI
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "100React API"
router.register('postAPI', PostAPI)



urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('api/', include(router.urls)),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]