from django.shortcuts import render, redirect
from .models import Book, Library, Author
from django.views.generic.detail import DetailView
from .models import Library

def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})
    return HttpResponse("List of books")

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
from django.contrib.auth import logout 
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

]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect("home")  # Redirect to homepage or dashboard after registration
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to a valid URL name
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login') 



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

# Check if the user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

# Check if the user is a Member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})