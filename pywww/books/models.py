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
  
  tags = models.ManyToManyField("tags.Tag", related_name="books")
  # Dodanie do książek tagów w relacji M2M oraz umożliwienia wyszukiwania książek po tagu dzięki related_name
  
  
  def __str__(self):
    # metoda specjalna służąca do przygotowania reprezentacji
    # tekstowej naszego obiektu. Zmiana w widoku jak i w PA
    return f"{self.id}.. {self.title}"
  