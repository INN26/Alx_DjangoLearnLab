from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)  

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):  
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

# Library Model with ManyToManyField to Book 
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="libraries")  

    def __str__(self):
        return self.name

# Librarian Model with OneToOneField to Library 
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

