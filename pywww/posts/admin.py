from django.contrib import admin
from django.db import models

from import_export import resources
from import_export.admin import ExportMixin

from .models import Post, Category
from common.admin import AdminImageWidget

# Register your models here.

class PostResource(resources.ModelResource):
  class Meta:
    model = Post
    # Informacja który model chcemy importować
    
  
@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin): # Wygląd i zachowanie w PA
  list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored']
  # Wyświetlenie dodatkowych informacji przy poście
  search_fields = ['id', 'title', 'content']
  # Panel do szukanie elementów
  list_filter = ['published', 'sponsored']
  # Możliwość ustawienia filtrów na pasku po lewej
  autocomplete_fields = ['tags']
  # Autouzupełnianie wpisywanych tagów (alternatywa dla filter_horizontal)
  # filter_horizontal = ['tags']
  # Umożliwia alternatywne wyświetlanie i dodawanie tagów do postó w PA
  resource_class = PostResource
  # Umożliwienie skorzystania z eksportu w PA dzięki klasie PostResource
  formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
  # Określamy widget ImageField (tak by wyświetał miniaturkę zdjęcia)



# admin.site.register(Post, PostAdmin)
# # Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)

admin.site.register(Category)
# Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
