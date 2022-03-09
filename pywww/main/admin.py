from django.contrib import admin

# Register your models here.
from main.models import UserProfile
from django.contrib.auth.models import User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ['id', 'bio']

admin.site.site_header = 'PyWWW Panel Administracyjny'
# Tytuł na niebiskim pasku w PA
admin.site.site_title = 'PyWWW'
# Nazwa karty po indexie index_title | site_title
admin.site.index_title = 'Witamy na stronie'
# Nazwa karty w głównej menu PA index_title | site_title