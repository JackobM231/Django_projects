from django.core.management.base import BaseCommand
from posts.utils import create_posts

class Command(BaseCommand):
  help = 'Create "n" posts in the database'
  
  def handle(self, *args, **options):               # Metoda handle odpowiada nam za wywołanie posta
    n = options.get('number')                       # options jest to słownik z którego chcemy pobrać (destination)
    create_posts(n)
    self.stdout.write('Posts have been created')    # Wyświetli informację w terminalu, stderr wyświetli błąd
  
  def add_arguments(self, parser):                  # parser podobne do argparsa
    parser.add_argument(
      '-n', '--number', type=int, default=10, dest='number', help='Number of posts to add'
    # skrócony argument, pełna nazwa argumentu, typ, wartość domyślna, destination, pomoc
    )
    
  
