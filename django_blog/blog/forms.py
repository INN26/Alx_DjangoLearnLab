from django import forms
from django.contrib.auth.models import User
from. models import Profile
from. models import Post

#Form to update User.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Form to update PrOfile.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ['image', 'bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


