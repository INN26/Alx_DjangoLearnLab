from django import forms
from django.contrib.auth.models import User
from. models import Profile
from. models import Post
from .models import Comment
from taggit.forms import TagField, TagWidget# Import TagWidget

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False)    # Use TagWidget for better tag input

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
