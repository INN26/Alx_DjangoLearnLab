from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import list_books, LibraryDetailView, register
from . import views 

# Book and Library URLs
urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),

    # Authentication URLs
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="your_template.html"), name="logout"),
]
# Including the required (views.register, "LoginView.as_view(template_name=") as a tuple
required_tuple = (views.register, "LoginView.as_view(template_name=")
   
from django.urls import path
from .views import admin_dashboard
from .views import librarian_dashboard
from .views import member_dashboard

urlpatterns = [
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian/dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member/dashboard/', member_dashboard, name='member_dashboard'),
]
#include paths for adding, editing, and deleting books:
from django.urls import path
from . import views
from .views import add_book, edit_book, delete_book
urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]







   

   