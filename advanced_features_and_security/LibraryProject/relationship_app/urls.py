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

   #registration
from django.contrib import admin   
from django.urls import path
from .views import admin_dashboard
from .views import librarian_dashboard
from .views import member_dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian/dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member/dashboard/', member_dashboard, name='member_dashboard'),
]
#include paths for adding, editing, and deleting books:
from django.urls import path
from .views import home 
from .views import add_book, edit_book, delete_book
urlpatterns = [
    path('', home, name='home'),  # Homepage URL
    path('add_book/', add_book, name='add_book'),  # Add Book URL
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),  # Edit Book URL
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),  # Delete Book URL
]




   
