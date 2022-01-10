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