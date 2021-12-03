from django.core.management.base import BaseCommand
from books.utils import create_books

class Command(BaseCommand):
  help = 'Create "n" books in the database'
  
  def handle(self, *args, **kwargs):
  # Metoda odpowiadająca za wywołanie posta
    n = kwargs.get('amount_of_books')
    create_books(n)
    self.stdout.write('Books have been created')
  
  def add_arguments(self, parser):
    parser.add_argument(
      '-n', '--number', type=int, default=1, dest='amount_of_books', help='Number of books to create'
    )