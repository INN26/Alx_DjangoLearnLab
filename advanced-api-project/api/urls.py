from django.urls import path
from .views import (
    CustomBookListView,
    CustomBookDetailView,
    CustomBookCreateView,
    CustomBookUpdateView,
    CustomBookDeleteView
)
#urls to connect the views with specific endpoints.
urlpatterns = [
    path('books/', CustomBookListView.as_view(), name='book-list'),
    path('books/create/', CustomBookCreateView.as_view(), name='book-create'),  # Create a book
    path('books/<int:pk>/', CustomBookDetailView.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/<int:pk>/update/', CustomBookUpdateView.as_view(), name='book-update'),  # Update a specific book
    path('books/<int:pk>/delete/', CustomBookDeleteView.as_view(), name='book-delete'), # delete a specific book

]
