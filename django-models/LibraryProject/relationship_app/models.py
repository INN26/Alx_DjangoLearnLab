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

# Role-Based Access Control in Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model): 'Admin', 'Member'
USER_ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
user = models.OneToOneField(User, on_delete=models.CASCADE)
role = models.CharField(max_length=20, choices= USER_ROLES)

def __str__(self):
        return f"{self.user.username} - {self.role}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()