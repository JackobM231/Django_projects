from django.db import models
from django.utils.timezone import now, timedelta

# Create your models here.


class CheckAgeMixin:
  """Mixin utworzony w celu umożliwnia dziedziczenia funkcji
     is_older_than_n_days wielu modelom"""
     
  def is_older_than_n_days(self, n=1):
    """ Sprawdzenie czy created jest starszy od now() - days"""
    delta = timedelta(days=n)
    return now() - self.created > delta
  

class Timestamp(models.Model, CheckAgeMixin):
  # Rozbicie klasy Post na mniejsze
  created = models.DateTimeField(auto_now_add=True)
  # data utworzenia - tylko przy utworzeniu
  modified = models.DateTimeField(auto_now=True)
  # data modyfikacji - zawsze po kliknięciu save

  class Meta:
    abstract = True
    # Poinformowanie django że klasa ta została utworzona wyłącznie w celu dziedziczenia
    # Django na jej postawie nie utworzy dodatkowej tabeli

class Post(Timestamp):
  title = models.CharField(max_length=255)
  # pole tekstowe o określonej długości
  content = models.TextField()
  # pole tekstowe o nieokreślonej długości
  published = models.BooleanField(default=False)
  # flaga true/false
  sponsored = models.BooleanField(default=False)
  # post sponsorowany
  author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
  # relacja postu z autorem którym jest id usera
  tags = models.ManyToManyField('tags.Tag', related_name='posts')
  # relacja wiele do wielu postu z tagami
  category = models.ManyToManyField('posts.Category', default=None, related_name='categories')
  # relacja wiele do wielu postu z kategoriami (w przyszłości użyć nazwy mnogiej)
  
  def __str__(self):
    # metoda specjalna służąca do przygotowania reprezentacji
    # tekstowej naszego obiektu. Zmiana w widoku jak i w PA
    return f"{self.id} {self.title}"


class Category(models.Model):
  name = models.CharField(unique=True, max_length=200)
  description = models.CharField(blank=True, max_length=500)
  # opis kategorii nieobowiązkowy z ograniczeniem do 500 znaków
  
  def __str__(self):
    if self.description:
      return f"{self.id}. {self.name} - {self.description}"
    else:
      return f"{self.id}. {self.name} - No description"
  
  class Meta:
    verbose_name_plural = "categories"