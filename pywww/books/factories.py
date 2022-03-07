import factory
from faker import Factory
from posts.factories import UserFactory

faker = Factory.create()


class AuthorFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = 'books.Author'
    django_get_or_create = ('name', 'birth_year')
    # Zakładamy że jeżeli jest autor o takim samym imieniu
    # oraz dacie urodzenia jest jedną osobą
    
  name = factory.LazyAttribute(lambda x: faker.name())
  birth_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
  biogram = factory.LazyAttribute(lambda x: faker.text(200))
  
  
class BookFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = 'books.Book'
    
  title = factory.LazyAttribute(lambda x: faker.text(30))
  description = factory.LazyAttribute(lambda x: faker.text(300))
  available = factory.LazyAttribute(lambda x: faker.boolean())
  publication_year = factory.LazyAttribute(lambda x: faker.date_of_birth().year)
  
  @factory.post_generation
  def authors(self, create, extracted, **kwargs):
  # W zależności czy post jest tworzony, czy edytowany
    if not create:
      # Edytowany
      return
    if extracted:
      for author in extracted:
        self.authors.add(author)
        
class BorrowFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = 'books.Borrow'
    
  user = factory.SubFactory(UserFactory)
  book = factory.SubFactory(BookFactory)
        
        

  