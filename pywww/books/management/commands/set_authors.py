from django.core.management.base import BaseCommand
from books.utils import set_books_authors

class Command(BaseCommand):
  help = "Set author of the book that hasn't one"
  
  def handle(self, *args, **kwargs):
  # Metoda odpowiadająca za wywołanie posta
    set_books_authors()
    self.stdout.write('Authors set')
