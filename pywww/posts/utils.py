from .models import Post
from faker import Faker
from random import randint
import sqlite3


def create_posts(n=10):
  fake = Faker("pl_PL")
  db = sqlite3.connect('db.sqlite3')
  # łączymy się z bazą danych
  cursor = db.cursor()
  cursor.execute('''SELECT count(distinct id) FROM auth_user''' )
  authors = cursor.fetchone()[0]
  # pobieramy liczbę użytkowników
  for i in range(n):
    d = fake.date_time_this_year()
    # zdefiniowana data utworzenia
    post = Post(
      title = fake.text(randint(10, 30))[:-1],
      content = fake.text(randint(50, 300)),
      published = fake.boolean(),
      created =  d,
      modified = fake.date_time_ad(None, None, d),
      sponsored = fake.boolean(),
      author_id = randint(1, authors)
    )
    
    post.save()
  
