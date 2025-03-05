from rest_framework import generics
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class BookViewSets(viewsets.ModelViewSet):
     #A ViewSet for viewing and editing book instances.
     queryset = Book.objects.all()
     serializer_class = BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        book = self.get_object(pk)
        if isinstance(book, Response):
            return book

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if isinstance(book, Response):
            return book

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)