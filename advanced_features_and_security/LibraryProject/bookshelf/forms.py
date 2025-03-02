from django import forms
from django.utils.html import strip_tags
from .models import Book

# Form definition 
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

# Preventing XSS attacks by filtering out malicious scripts.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get("title")

        # Strip any HTML tags to prevent XSS
        sanitized_title = strip_tags(title)

        if sanitized_title != title:  # If any tags were removed, it was malicious input
            raise forms.ValidationError("Invalid characters detected in title.")

        return sanitized_title