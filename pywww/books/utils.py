from .models import Book, Author
from faker import Faker
from random import randint
import datetime

def create_books(n=5):
  # Definiowanie domyślnej liczby książek w tym miejscu nie ma sensu. 
  # Priorytetem jest liczba z folderu commands
  fake = Faker()
  authors = (Author.objects.all())
  num_of_authors = len(authors)
  for i in range(n):
    book = Book(
      title = fake.text(randint(6, 30))[:-1],
      description = fake.text(randint(15, 300)),
      available = fake.boolean(),
      created = fake.past_date(),
      publication_year = randint(1945, 2021),
    )
    book.save()
    book.author.add(authors[randint(1, num_of_authors)-1])
    # Automatyczne dobranie losowego autora
    

def create_authors(n):
  fake = Faker()
  now = (datetime.datetime.now()).year
  for i in range(n):
    birth = randint(1850, 2000)
    death = (birth + randint(20,85))
    if death > now:
      death = None
      
    author = Author(
      name = fake.name(),
      birth_year = birth,
      death_year = death,
      biogram = fake.text(randint(15, 300)),
    )
    author.save()
    

def set_books_authors():
  books = Book.objects.filter(author__name__exact='')
  # Książki których nazwa autora to dokładnie ''
  authors = (Author.objects.all())
  # Wszyscy autorzy

  for book in books:
    author = authors[randint(0, len(authors)-1)]
    # Losowo wybrany autor
    book.author.add(author)
  
  