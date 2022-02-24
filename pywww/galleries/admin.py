from django.contrib import admin

from .models import Gallery, Photo

# Register your models here.

# class PhotoInline(admin.TabularInline): alternatywny wygląd
class PhotoInline(admin.StackedInline):
  model = Photo
  fields = ['title', 'slug', 'short_description', 'image', 'status', 'created', 'modified']
  # Pola które będą widoczne w trakcie dodawania nowych zdjęć
  readonly_fields = ['slug', 'created', 'modified']
  # Pola do odczytu po reszcie pól
  extra = 1
  # Liczba pól odpowiadających za dodanie nowych zdjęć

# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
#   pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
  fields = ['title', 'slug', 'description', 'status', 'created', 'modified']
  readonly_fields = ['slug', 'created', 'modified']
  inlines = [PhotoInline]
  # Zapewnia wyświetlanie zdjęć należących do tej galerii w PA