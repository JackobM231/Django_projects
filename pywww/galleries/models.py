import string
import random

from django.db import models
from django.utils.text import slugify
from common.models import Timestamp, SlugMixin

from sorl.thumbnail import ImageField

# Create your models here.

# def get_random_text(n):
#   letters = string.ascii_letters
#   return ''.join(random.choice(letters) for i in range(n))

class Gallery(Timestamp, SlugMixin):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=1500, blank=True, null=True)
  # slug = models.SlugField(unique=True, max_length=150)
  
  def __str__(self):
    return self.title
  
  # def save(self, *args, **kwargs):    # Zastąpione dziedziczenuiem z common
  #   if self._state.adding and not self.slug:
  #     slug = slugify(self.title)
  #     slugs = self.__class__.objects.values_list('slug', flat=True)
  #     if slugs:
  #       while True:
  #         if slug in slugs:
  #           slug += get_random_text(5)
  #         else:
  #           break
  #     self.slug = slug
  #   return super().save(*args, **kwargs)
      


def upload_to(instance, filename):
  return f'galleries/{instance.gallery.slug}/{filename}'
  
class Photo(Timestamp, SlugMixin):
  title = models.CharField(max_length=100)
  # slug = models.SlugField(unique=True, max_length=150)
  short_description = models.CharField(max_length=300, blank=True, null=True)
  image = ImageField(upload_to=upload_to)
  gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='photos')
  source = models.CharField(max_length=512, blank=True, null=True)
  
  def __str__(self):
    return self.title 