from django.contrib import admin
from .models import Book

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'publication_year', 'created']
  search_fields = ['title', 'author', 'description']
  list_filter = ['available']

admin.site.register(Book, PostAdmin)
# rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
