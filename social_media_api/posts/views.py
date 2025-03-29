from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
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
        return Post.objects.filter(author__in= following_users ).order_by('-created_at')