from django.contrib import admin
from django.contrib.auth.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "gender", "language", "currency", "is_super_host")
    list_filter = ("language", "currency", "is_super_host")
