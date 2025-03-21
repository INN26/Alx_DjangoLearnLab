from django.db import models
from django.utils.timezone import now  # Import Django's timezone utility

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)  # Use `default=now` instead of `auto_now_add=True`
    updated_at = models.DateTimeField(auto_now=True)