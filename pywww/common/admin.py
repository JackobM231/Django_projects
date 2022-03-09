from django.contrib import admin

from django.contrib.admin.widgets import AdminFileWidget
# from django.utils.safestring import mark_safe -- oznacza wpis jako bezpieczny 
# do wykorzystania bezpośrednio w naszym widgecie
from sorl.thumbnail import get_thumbnail

# Register your models here.

class AdminImageWidget(AdminFileWidget):
  # Klasa pozwalająca na wyświetlanie miniaturki zdjęcia w PA
  
  def render(self, name, value, attrs=None, renderer=None):
    output = []
    if value and getattr(value, 'url', None):
      t = get_thumbnail(value, '150') # Nowy cash obrazu o rozm.150
      output.append(f'<a href="{value.url}" target="_blank"><img src="{t.url}"></a>')
    output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
    # return mark_safe(''.join(output))
    return ''.join(output)