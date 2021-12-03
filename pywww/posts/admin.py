from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin): # Wygląd i zachowanie w PA
  list_display = ['id', 'title', 'created', 'modified', 'published', 'sponsored']
  # Wyświetlenie dodatkowych informacji przy poście
  search_fields = ['id', 'title', 'content']
  # Panel do szukanie elementów
  list_filter = ['published', 'sponsored']
  # Możliwość ustawienia filtrów na pasku po lewej

admin.site.register(Post, PostAdmin)
# rejestracja modeli w panelu administracyjnym (sprawienie że są widoczne)
