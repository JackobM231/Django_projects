from django.db import models
from common.models import Timestamp


# Create your models here.
class Author(Timestamp):
  name = models.CharField(max_length=200)
  birth_year = models.IntegerField()
  death_year = models.IntegerField(blank=True, null=True)
  # blank=True pole może zostać pominięte(puste), null=True dopuszczamy by komórka miała wartość NULL
  biogram = models.TextField(blank=True)
  
  def __str__(self):
    if self.birth_year and self.death_year:
      return f"{self.name} ({self.birth_year} - {self.death_year})"
    return f"{self.name}"


class Book(Timestamp):
  title = models.CharField(max_length=255)
  # tytuł książki z ograniczeniem znaków
  description = models.TextField(max_length=1500)
  # opis książki z ograniczeniem znaków
  available = models.BooleanField(default=True)
  # flaga true/false
  publication_year = models.SmallIntegerField(help_text="Please use this format 'yyyy'", blank=True, null=True)
  # rok publikacji, może być pusty
  author = models.ManyToManyField(Author, related_name="books")
  # autor książki - możliwe wielu autorów
  
  tags = models.ManyToManyField("tags.Tag", related_name="books")
  # Dodanie do książek tagów w relacji M2M oraz umożliwienia wyszukiwania książek po tagu dzięki related_name
  
  
  def __str__(self):
    # metoda specjalna służąca do przygotowania reprezentacji
    # tekstowej naszego obiektu. Zmiana w widoku jak i w PA
    return f"{self.id}. {self.title}"
  
  

  
  