from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import Post, Category

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
  resource_class = PostResource
  # Umożliwienie skorzystania z eksportu w PA dzięki klasie PostResource

# admin.site.register(Post, PostAdmin)
# # Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)

admin.site.register(Category)
# Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
