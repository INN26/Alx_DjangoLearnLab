from rest_framework import serializers
from .models import Author, Book

#Creating custom Serializers
# Serializers convert model instances into JSON format for APIs and handle validation.
class BookSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Book
        fields = ['__all__']
#Custom validation to ensure the publication_year is not in the future.
    from datetime import date
    def validate(date, publication_year):
         if publication_year > date.today().year:
               raise serializers.ValidationError("Publication year cannot be in the future.")
         return publication_year


 
#AuthorSerializer includes a nested representation of books.  
#Nested Serializers for Related Objects  
class AuthorSerializer(serializers.ModelsSerializer): 
    class Meta:
         model = Author
         fields = ['name']

    class BookSerializer(serializers.ModelsSerializer):
                 books = BookSerializer(many = True, read_only = True) #nested serialiser
                 class Meta:
                    model = Book
                    fields = ['name', 'books']
 