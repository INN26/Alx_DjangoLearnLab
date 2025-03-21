from django.urls import path, include
from.import views
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.urls import path
from .models import Post
from .views import search_posts
from blog.views import TaggedItemView
from django.contrib.auth import views as auth_views
from .views import PostByTagListView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('tags/<slug:tag_slug>/', TaggedItemView.as_view(), name='posts_by_tag'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', TaggedItemView.as_view(model=Post), name='posts_by_tag'),
    path('tags/<str:tag_name>/', PostByTagListView.as_view(), name='posts_by_tag'),
   
]
