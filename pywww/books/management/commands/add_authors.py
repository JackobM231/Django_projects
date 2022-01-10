from django.core.management.base import BaseCommand
from books.utils import create_authors

class Command(BaseCommand):
  help = 'Create "n" authors in the database'
  
  def handle(self, *args, **kwargs):
  # Metoda odpowiadająca za wywołanie posta
    n = kwargs.get('number_of_authors')
    create_authors(n)
    self.stdout.write('Authors have been created')
  
  def add_arguments(self, parser):
    parser.add_argument(
      '-n', '--number', type=int, default=1, dest='number_of_authors', help='Number of authors to create'
    )