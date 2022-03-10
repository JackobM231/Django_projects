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

# Można władować do common
class HasTagsFilter(admin.SimpleListFilter):
  '''Klasa odpowiedzialna za możliwość
  filtrowania ilości tagów przypisanych 
  do posta
  '''
  title = 'Liczba tagów'
  parameter_name = '_tags_count'
  
  def lookups(self, request, model_admin):
    return (('Yes', 'Tak'), ('No', 'Nie'))

  def queryset(self, request, queryset):
    value = self.value()
    if value == 'Yes':
      return queryset.filter(_tags_count__gt=0)
    elif value == 'No':
      return queryset.filter(_tags_count=0)
    return queryset
  
  
@admin.register(Post)
class PostAdmin(ExportMixin, admin.ModelAdmin): # Wygląd i zachowanie w PA
  list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored', 'tags_count']
  # Wyświetlenie dodatkowych informacji przy poście
  search_fields = ['id', 'title', 'content']
  # Panel do szukanie elementów
  list_filter = ['published', 'sponsored', HasTagsFilter]
  # Możliwość ustawienia filtrów na pasku po lewej
  autocomplete_fields = ['tags']
  # Autouzupełnianie wpisywanych tagów (alternatywa dla filter_horizontal)
  # filter_horizontal = ['tags']
  # Umożliwia alternatywne wyświetlanie i dodawanie tagów do postó w PA
  resource_class = PostResource
  # Umożliwienie skorzystania z eksportu w PA dzięki klasie PostResource
  formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
  # Określamy widget ImageField (tak by wyświetał miniaturkę zdjęcia)
  
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    queryset = queryset.annotate(_tags_count=models.Count('tags'))
    return queryset
  
  def tags_count(self, obj):
    return obj._tags_count
  
  tags_count.admin_order_field = '_tags_count'
  tags_count.short_description = 'Liczba tagów'


# admin.site.register(Post, PostAdmin)
# # Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)

admin.site.register(Category)
# Rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
