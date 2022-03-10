from django.contrib import admin
from django.db import models
from django.db.models import Count

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


class HasPhotoFilter(admin.SimpleListFilter):
  title = 'Ilość zdjęć'
  parameter_name = 'photos_count'
  
  def lookups(self, request, model_admin):
    '''
    Zwraca listę tupli, Pierwszy element każdej tupli
    jest zapisaną wartością dla opicji która pojawi
    się w zaytaniu URL. Drugi element jest zapisem
    dla człowieka który wyświetli się z prawej strony
    paska
    '''
    return (
      ('Yes', 'Tak'),
      ('No', 'Nie')
    )
    
  def queryset(self, request, queryset):
    '''
    Zwraca przefiltrowany zestaw zapytań na podstawie
    wartości podanej w ciągu zapytania i można go
    pobrać przez 'self.value()'
    '''
    value = self.value()
    if value == 'Yes':
      return queryset.filter(_photos_count__gt=0)
    elif value == 'No':
      return queryset.filter(_photos_count=0)
    return queryset


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
  list_display = ['title', 'photos_count']
  # Informacje widoczne w PA po wejściu w aplikację
  readonly_fields = ['slug', 'created', 'modified']
  inlines = [PhotoInline]
  # Zapewnia wyświetlanie zdjęć należących do tej galerii w PA
  list_filter = [HasPhotoFilter]
  # fields = ['title', 'slug', 'description', 'status', 'created', 'modified']
  # # Pola widoczne po wejściu w konkretną galerię
  fieldsets = (
    ('', {
      'fields': ('title', 'slug',),
    }),
    ('Opis', {
      'fields': ('description',),
      'description': "Tekst opisujący pole"
    }),
    ('Status', {
      'fields': ('status', 'created', 'modified',),
    }),
  )
  
  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    queryset = queryset.annotate(_photos_count=Count('photos'))
    # Zlieczenie zdjęć znajdujących się w poszczególnych galeriach
    return queryset
  
  def photos_count(self, obj):
    # Nowa kolumna zawierająca ilość zdjęć znajdujących się w galeriach
    return obj._photos_count
  
  photos_count.admin_order_field = '_photos_count'
  # Możliwość sortowania po kolumnie photos_count
  photos_count.short_description = 'Ilość zdjęć'
  # Zmiana wyświetlanej nazwy kolumny w PA
  

  
