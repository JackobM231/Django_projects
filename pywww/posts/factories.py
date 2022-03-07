import factory
from faker import Factory

faker = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = 'auth.User'
    django_get_or_create = ('email',)
    
  username = factory.Sequence(lambda n: f'user{n}')
  email = factory.Sequence(lambda n: f'user{n}@gmail.com')
  first_name = factory.LazyAttribute(lambda x: faker.first_name())
  last_name = factory.LazyAttribute(lambda x: faker.last_name())
  # password = factory.LazyAttribute(lambda obj: '%s123' % obj.username)
  password = '123'
  

class PostFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = 'posts.Post'
    
  title = factory.Sequence(lambda n: f'post {n}')
  content = factory.Sequence(lambda n: f'Lorem ipsum {n}')
  # content = factory.LazyAttribute(lambda x: fake.text(150))
  published = factory.LazyAttribute(lambda x: faker.boolean())
  sponsored = factory.LazyAttribute(lambda x: faker.boolean())
  author = factory.SubFactory(UserFactory)
  image = factory.django.FileField(filename='image.png')
  