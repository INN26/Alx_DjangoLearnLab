from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    books = models.ManyToManyField(Book)  # Fixed reference to Book

# Librarian Model with OneToOneField to Library 
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

# Role-Based Access Control in Django
class UserProfile(models.Model):
    USER_ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "userprofile"):  
        instance.userprofile.save()

# Custom User Manager
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()  

    def __str__(self):
        return self.username

    class Meta: 
        permissions = [
            ("can_view_dashboard", "Can View Dashboard"),
            ("can_edit_profile", "Can Edit Profile"),
        ]