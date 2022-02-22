import string
import random
from django.db import models
from django.utils.timezone import now, timedelta
from django.utils.text import slugify

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
  # Data utworzenia - tylko przy utworzeniu
  modified = models.DateTimeField(auto_now=True)
  # Data modyfikacji - zawsze po kliknięciu save

  class Meta:
    abstract = True
    # Poinformowanie django że klasa ta została utworzona wyłącznie w celu dziedziczenia
    # Django na jej postawie nie utworzy dodatkowej tabeli
    
    
    
def get_random_text(n):
  letters = string.ascii_letters
  return ''.join(random.choice(letters) for i in range(n))

class SlugMixin(models.Model):
  SLUG_BASE_FIELD = 'title'
  # Dodajemy zmienną po której będzie tworzony slug
  SLUG_SUFFIX_LEN = 3
  # Dodajemy zmienna odpowiedzialną za ilość dodatkowych znaków w slug
  slug = models.SlugField(max_length=100, unique=True)
  
  class Meta:
    abstract = True
    
  def save(self, *args, **kwargs):
    if self._state.adding and not self.slug:
      slug = slugify(getattr(self, self.SLUG_BASE_FIELD))
      slugs = self.__class__.objects.filter(slug=slug).values_list('slug', flat=True)
      if slugs:
        while True:
          if slug in slugs:
            slug += get_random_text(self.SLUG_SUFFIX_LEN)
          else:
            break
      self.slug = slug 
    return super().save(*args, **kwargs)