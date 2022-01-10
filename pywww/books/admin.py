from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book

# Register your models here.
class BookResource(resources.ModelResource):
  class Meta:
    model = Book
    # dane którego modelu będzie można exportować

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'publication_year', 'created']
  search_fields = ['title', 'author', 'description']
  list_filter = ['available']
  resource_class = BookResource
  # umożliwienie eksportu

# admin.site.register(Book, BookAdmin)
# # rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
# zamiast tego mamy już @admin.register(Book)
