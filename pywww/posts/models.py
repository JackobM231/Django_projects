from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=255)
  # pole tekstowe o określonej długości
  content = models.TextField()
  # pole tekstowe o nieokreślonej długości
  published = models.BooleanField(default=False)
  # flaga true/false
  created = models.DateTimeField(auto_now_add=True)
  # data utworzenia - tylko przy utworzeniu
  modified = models.DateTimeField(auto_now=True)
  # data modyfikacji - zawsze po kliknięciu save
