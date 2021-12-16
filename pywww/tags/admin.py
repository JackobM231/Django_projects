from django.contrib import admin
from .models import Tag

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}
  # Dzięki temu można dodwać tagi w PA podając wyłącznie nazwę, a slug jest tworzony na jego podstawie