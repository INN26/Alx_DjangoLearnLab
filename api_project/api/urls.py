from django.urls import path, include
from .views import BookList
#Configure the Router.
from rest_framework.routers import DefaultRouter
from .views import BookViewSets

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'books-all', BookViewSets, basename='book_all' )

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),# Maps to the BookList view

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]




