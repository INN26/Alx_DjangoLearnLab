from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)
#urls to connect the views with specific endpoints.
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update a specific book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'), # delete a specific book

]
