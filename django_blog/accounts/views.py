from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import UserRegisterForm

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post-list')  # Redirect to blog home
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# User Profile View
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('post-list')
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

