from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model extending Django’s AbstractUser
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    
    # Many-to-Many relationship for followers and following using an intermediate model
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        through="Follow",
        through_fields=("user_from", "user_to"),
    )

    def __str__(self):
        return self.username

# Intermediate Model to handle following relationships
class Follow(models.Model):
    user_from = models.ForeignKey(CustomUser, related_name="following_rel", on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name="followers_rel", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_from", "user_to")

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"
