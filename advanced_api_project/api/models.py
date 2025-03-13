from django.db import models

# Defining data models.
class Author(models.Model):
    name = models.CharField(max_length=200) #authors name

    def __str__(self):
        return self.name
    
class Book(models.Model):
    
    title = models.CharField(max_length=200) #the book title
    publication_year = models.IntegerField() 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')#one to one relationship
     
    def __str__(self):
        return self.title
    
     
     
