from django.contrib import admin
from django.db import models

from .models import Gallery, Photo
from common.admin import AdminImageWidget

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
  formfield_overrides = {
    models.ImageField: {'widget': AdminImageWidget}
    # Określamy widget ImageField (tak by wyświetał miniaturkę zdjęcia)
  }

# @admin.register(Photo)
# class PhotoAdmin(admin.ModelAdmin):
#   pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
  fields = ['title', 'slug', 'description', 'status', 'created', 'modified']
  readonly_fields = ['slug', 'created', 'modified']
  inlines = [PhotoInline]
  # Zapewnia wyświetlanie zdjęć należących do tej galerii w PA