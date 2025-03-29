from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Like, Post
from posts.serializers import LikeSerializer
from notifications.utils import create_notification
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views import View

from .serializers import PostSerializer, CommentSerializer

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
        try:
            post = Post.objects.get(pk=pk)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if created:
                create_notification(request.user, post.author, "liked your post", post)
                return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)
            return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        """Unlike a post."""
        try:
            like = Like.objects.get(user=request.user, post_id=pk)
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
class NotificationListView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"notifications": []})  # Placeholder response