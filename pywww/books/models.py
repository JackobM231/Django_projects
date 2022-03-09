from django.db import models
from common.models import Timestamp

from sorl.thumbnail import ImageField

# Create your models here.
class Author(Timestamp):
  class Meta:
    verbose_name = "Autor"
    verbose_name_plural = "Autorzy"
    # Zmiana wyświetlania nazwy w PA
  
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
  class Meta:
    verbose_name = "Książka"
    verbose_name_plural = "Książki"
    
  title = models.CharField(max_length=255)
  # tytuł książki z ograniczeniem znaków
  description = models.TextField(max_length=1500)
  # opis książki z ograniczeniem znaków
  available = models.BooleanField(default=True)
  # flaga true/false
  publication_year = models.SmallIntegerField(help_text="Please use this format 'YYYY'", blank=True, null=True)
  # rok publikacji, może być pusty
  authors = models.ManyToManyField(Author, related_name="books")
  # autor książki - możliwe wielu autorów
  tags = models.ManyToManyField("tags.Tag", blank=True, related_name="books")
  # Dodanie do książek tagów w relacji M2M oraz umożliwienia wyszukiwania książek po tagu dzięki related_name
  image = ImageField(upload_to='books/covers/%Y/%m/%d', blank=True, null=True)
  # możliwość dodania obrazu do pliku, plik nie jest wymagany w formularzu (blank=True) oraz nie jest wymagany w BD (null=False)
  
  def __str__(self):
    # metoda specjalna służąca do przygotowania reprezentacji
    # tekstowej naszego obiektu. Zmiana w widoku jak i w PA
    return f"{self.id}. {self.title}"
  
  
class Borrow(models.Model):
  book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='borrows')
  #related_name Nazwa używana do relacji z powiązanego obiektu do tego (z Book do Borrow)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='borrows')
  borrow_date = models.DateTimeField(auto_now_add=True)
  return_date = models.DateTimeField(blank=True, null=True)
  

  
  