from django.urls import path, include
from .views import BookList, BookDetailView
#Configure the Router.
from rest_framework.routers import DefaultRouter
from .views import BookViewSets
from rest_framework.authtoken.views import obtain_auth_token
# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'books-all', BookViewSets, basename='book_all' )

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),# Maps to the BookList view

      # Retrieve, update, or delete a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    
    #Generate and Use Tokens
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]