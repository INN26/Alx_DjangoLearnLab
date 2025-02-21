from django.urls import path
from .views import list_books, LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import register

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(template_name="your_template.html"), name="logout"), 
    path(views.register, "LoginView.as_view(template_name=")
]

