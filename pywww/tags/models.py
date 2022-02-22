from django.db import models
from django.utils.text import slugify

from common.models import SlugMixin

# Create your models here.

'''
class Tag(models.Model):
  name = models.CharField(unique=True, max_length=100)
  # Tworzymy nazwę tagu, która ma być unikalna o max dł. 100
  slug = models.SlugField(unique=True, max_length=100)
  # Tworzymy slug tagu, który ma być unikalny o max dł. 100
  
  def __str__(self):
    return f"{self.name} with slug: {self.slug}"
  # Sposób wyświetlenia w Panelu Administracyjnym po wejściu w Tags
  
  
  """Nadpisujemy metodę save by uzupełniała
  wartość  pola slug przy zapisie"""
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.name)
    return super().save(*args, **kwargs)
'''
class Tag(SlugMixin):
  SLUG_BASE_FIELD = 'name'
  
  name = models.CharField(unique=True, max_length=100)
  
  def __str__(self):
    return f'{self.name}'