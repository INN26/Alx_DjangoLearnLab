from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

#user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully')
            return redirect('profile')
        else:
            form = UserRegisterForm()
        return render(request, 'blog/register.html', {'form': form})
        
#user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, 'blog/login.html')
    
#user logout
def user_logout(request):
    logout(request)
    messages.success(request, "you have logged out")
    return redirect('login')

#custom decorator
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.profile)
        if user_form.is_valid() and  profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return render('profile')
    else:
        user_form = UserUpdateForm(instance= request.user)
        profile_form = ProfileUpdateForm(instance =request.user.profile)
        
    return render(request, 'blog/profile.html')


