from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):  
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

# Library Model with ManyToManyField to Book 
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

# Librarian Model with OneToOneField to Library 
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

# Function to get default user
def get_default_user():
    User = get_user_model()
    user = User.objects.first()
    return user.id if user else None  

# Role-Based Access Control
class UserProfile(models.Model):
    USER_ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(  settings.AUTH_USER_MODEL,on_delete=models.CASCADE)   
    role = models.CharField(max_length=20, choices=USER_ROLES, default="Member")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"  

# Signals to auto-create UserProfile
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "userprofile"):
        instance.userprofile.save()
    
