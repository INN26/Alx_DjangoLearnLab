from rest_framework import viewsets, permissions, status, generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View

from .models import Post, Comment, Like
from notifications.models import Notification  # Ensure Notification model is imported
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve posts from followed users."""
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """Like a post."""
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # Create a notification for the post author
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

        return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """Unlike a post."""
        like = generics.get_object_or_404(Like, user=request.user, post_id=pk)
        like.delete()
        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)

class NotificationListView(View):
    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
        data = [
            {
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for notification in notifications
        ]
        return JsonResponse({"notifications": data}, safe=False)
    