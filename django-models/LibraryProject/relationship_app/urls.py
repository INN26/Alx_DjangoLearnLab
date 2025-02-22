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
   













   

   