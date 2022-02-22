from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book, Author

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

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  exclude = [Author]
  list_display = ['id', 'title', 'publication_year', 'created']
  search_fields = ['title', 'author', 'description']
  list_filter = ['available']
  autocomplete_fields = ['tags']
  # Automatyczne uzupełnianie tagów
  resource_class = BookResource
  # Umożliwienie eksportu
  inlines = [BookAuthorInline]

# admin.site.register(Book, BookAdmin)
# # rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
# zamiast tego mamy już @admin.register(Book)


