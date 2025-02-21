from django.urls import path
from .views import LibraryDetailView, book_list
from .views import list_books

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
   path('books/', list_books, name='list_books'),  # Optional: Book list page
]



