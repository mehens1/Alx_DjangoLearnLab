from rest_framework import viewsets, permissions, generics
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get the users that the current user follows
        followed_users = user.following.all()  
        # Return posts from the followed users
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        # Check if the post is already liked
        if not Like.objects.filter(user=user, post=post).exists():
            Like.objects.create(user=user, post=post)
            return Response({'status': 'post liked'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'post already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        # Check if the post is liked and remove the like
        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
            return Response({'status': 'post unliked'}, status=status.HTTP_200_OK)
        return Response({'status': 'post not liked'}, status=status.HTTP_400_BAD_REQUEST)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()  # Get the users that the current user follows
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')