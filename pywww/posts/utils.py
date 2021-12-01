from .models import Post
from faker import Faker
from random import randint


def create_posts(n=10):
  fake = Faker("pl_PL")
  for i in range(n):
    d = fake.date_time_this_year()
    # zdefiniowana data utworzenia
    post = Post(
      title = fake.text(randint(10, 30)),
      content = fake.text(randint(50, 300)),
      published = fake.boolean(),
      created =  d,
      modified = fake.date_time_ad(None, None, d),
      sponsored = fake.boolean()
    )
    
    post.save()
  
