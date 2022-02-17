from django.db import models
from common.models import Timestamp

from sorl.thumbnail import ImageField

# Create your models here.

class Post(Timestamp):
  title = models.CharField(verbose_name='Tytuł', max_length=255)
  # pole tekstowe o określonej długości
  content = models.TextField(verbose_name='Treść')
  # pole tekstowe o nieokreślonej długości
  published = models.BooleanField(verbose_name='Opublikowany', default=False)
  # flaga true/false
  sponsored = models.BooleanField(verbose_name='Sponsorowany', default=False)
  # post sponsorowany
  author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="posts")
  # relacja postu z autorem którym jest id usera
  tags = models.ManyToManyField('tags.Tag', related_name='posts')
  # relacja wiele do wielu postu z tagami
  category = models.ManyToManyField('posts.Category', default=None, related_name='categories')
  # relacja wiele do wielu postu z kategoriami (w przyszłości użyć nazwy mnogiej)
  example_file = models.FileField(upload_to='posts/examples/', blank=True, null=True)
  # możliwość dodania ścieżki pliku, który później będziemy mogli pobrać
  image = ImageField(upload_to='posts/images/%Y/%m/%d', blank=True, null=True)
  # możliwość dodania obrazu do pliku, plik nie jest wymagany w formularzu (blank=True) oraz nie jest wymagany w BD (null=False)
  
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
    