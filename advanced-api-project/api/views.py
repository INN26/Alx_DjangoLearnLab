from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from . serializers import BookSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
#setting generic views for the Book model to handle CRUD operations.
#A CreateView for adding a new book.
class CustomBookCreateView(generics.CreateAPIView):
    querry_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  #auth to adding a new book.
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

#ListView for retrieving all books.
class CustomBookListView(generics.ListAPIView):
    querry_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # anyone can view
     
#A DetailView for retrieving a single book by ID.
class CustomBookDetailView(generics.DetailAPIView):
    querry_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # auth for retrieving a single book by ID.

#An UpdateView for modifying an existing book.
class CustomBookUpdateView(generics.UpdateView):
    querry_set = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #for modifying an existing book.
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
#A DeleteView for removing a book.
class CustomBookDeleteView(generics.DeleteAPIView):
     querry_set = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly] # auth for removing a book.



