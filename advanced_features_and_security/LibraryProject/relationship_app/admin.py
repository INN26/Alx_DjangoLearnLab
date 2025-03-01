from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

  #custom ModelAdmin class that includes configurations for the additional fields in your user model.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "date_of_birth", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)