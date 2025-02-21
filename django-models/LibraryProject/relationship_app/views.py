from django.shortcuts import render
from .models import Book, Library, Author
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def add_author(name):
    author, created = Author.objects.get_or_create(name=name)
    if created:
        print(f"Author '{name}' added successfully!")
    else:
        print(f"Author '{name}' already exists.")
       
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView   
from django.contrib.auth import login   
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

#UserCreationFormform and the CreateViewclass-based view to handle user registration.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#utilities for handling user login and logout processes.
urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name= 'logout'),
    path("UserCreationForm()", "relationship_app/register.html")
]
