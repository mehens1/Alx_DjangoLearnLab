from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import FeedView
from .views import UserFeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'feed', FeedView, basename='feed')


urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('', include(router.urls)),
]
