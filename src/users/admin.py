from django.contrib import admin
from django.contrib.auth.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

