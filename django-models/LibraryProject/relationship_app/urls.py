from django.urls import path
from .views import LibraryDetailView, book_list
from .views import list_books

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('books/', book_list, name='book-list'),  # Optional: Book list page
]