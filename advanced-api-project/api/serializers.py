from rest_framework import serializers
from .models import Author, Book
import datetime

#Creating custom Serializers
# Serializers convert model instances into JSON format for APIs and handle validation.
class BookSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Book
        fields = '__all__'
#Custom validation to ensure the publication_year is not in the future.

    def validate(self, publication_year):
         current_year = datetime.date.today().year
         if publication_year > current_year:
               raise serializers.ValidationError("Publication year cannot be in the future.")
         return publication_year
#AuthorSerializer includes a nested representation of books.  
#Nested Serializers for Related Objects  
class AuthorSerializer(serializers.ModelsSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']']    