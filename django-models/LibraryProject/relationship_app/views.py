from django.shortcuts import render
from .models import Book, Library, Author
from .models import Library
from django.views.generic.detail import DetailView

def book_list(request):
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