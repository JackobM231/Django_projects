from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  # tytuł książki z ograniczeniem znaków
  description = models.TextField(max_length=1500)
  # opis książki z ograniczeniem znaków
  available = models.BooleanField(default=True)
  # flaga true/false
  publication_year = models.SmallIntegerField(help_text="Please use this format 'yyyy'", blank=True, null=True)
  # rok publikacji, może być pusty
  author = models.CharField(max_length=255)
  # autor książki
  created = models.DateTimeField(auto_now_add=True)
  # data utworzenia - tylko przy utworzeniu
  