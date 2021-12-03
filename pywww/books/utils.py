from .models import Book
from faker import Faker
from random import randint

def create_books(n=5):
  fake = Faker()
  for i in range(n):
    book = Book(
      title = fake.text(randint(6, 30))[:-1],
      description = fake.text(randint(15, 300)),
      available = fake.boolean(),
      author = fake.name(),
      created = fake.past_date(),
      publication_year = randint(1945, 2021),
    )
    
    book.save()
