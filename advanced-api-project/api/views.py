from django.shortcuts import render
from rest_framework import viewsets,  permissions, filters
from .models import Book
from . serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django_filters import rest_framework
#setting generic views for the Book model to handle CRUD operations.
#A CreateView for adding a new book.
class CustomBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can add a new book.
    filter_backends = [filters.SearchFilter]
    SearchFilter_fields = ['title']

#ListView for retrieving all books.
class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view books.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    SearchFilter_fields = ['title', 'author']  # Assuming 'author' is a field in Book model.
    OrderingFilter_fields = ['title', 'publication_year']  # Assuming 'published_date' exists.
     
#A DetailView for retrieving a single book by ID.
class CustomBookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # auth for retrieving a single book by ID.

#An UpdateView for modifying an existing book.
class CustomBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify a book.
    filter_backends = [filters.SearchFilter]
    SearchFilter_fields = ['title']

#A DeleteView for removing a book.
class CustomBookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # O



