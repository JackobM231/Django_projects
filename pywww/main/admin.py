from django.contrib import admin

# Register your models here.
from main.models import UserProfile
from django.contrib.auth.models import User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ['id', 'bio']
  