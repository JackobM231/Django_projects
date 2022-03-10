from django.contrib import admin
from django.db import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book, Author
from common.admin import AdminImageWidget

# Register your models here.

class BookAuthorInline(admin.StackedInline):
  model = Book.authors.through
  extra = 1
  
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass
  
  
class BookResource(resources.ModelResource):
  class Meta:
    model = Book
    # dane którego modelu będzie można exportować
    
class HasTagsFilter(admin.SimpleListFilter):
  '''Klasa odpowiedzialna za możliwość
  filtrowania ilości tagów przypisanych 
  do ksiązki
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
  
  
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  exclude = [Author]
  list_display = ['id', 'title', 'publication_year', 'created', 'tags_count']
  search_fields = ['title', 'author', 'description']
  list_filter = ['available', HasTagsFilter]
  autocomplete_fields = ['tags']
  # Automatyczne uzupełnianie tagów
  resource_class = BookResource
  # Umożliwienie eksportu
  inlines = [BookAuthorInline]
  formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}
  # Wyświetlanie miniaturki zdjęcia
  
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    queryset = queryset.annotate(_tags_count=models.Count('tags'))
    return queryset
  
  def tags_count(self, obj):
    return obj._tags_count
  
  tags_count.admin_order_field = '_tags_count'
  # Możliwość sortowania po nowo utworzonej kolumnie
  tags_count.short_description = 'Liczba tagów'
  # Zdefiniowanie wyświetlanej nazwy w PA

# admin.site.register(Book, BookAdmin)
# # rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
# zamiast tego mamy już @admin.register(Book)


