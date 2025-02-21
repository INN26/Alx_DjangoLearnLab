from django.urls import path
from .views import list_books, LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from . import views
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path(views.register, "LogoutView.as_view(template_name="), 
    path(views.register, "LoginView.as_view(template_name=")
]