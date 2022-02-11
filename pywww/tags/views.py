from dal import autocomplete

from tags.models import Tag
# Create your views here.

class TagAutocomplete(autocomplete.Select2QuerySetView):
  def get_queryset(self):
    if not self.request.user.is_authenticated:
      return Tag.objects.none()
    
    qs = Tag.objects.all()
    
    if self.q:
      qs = qs.filter(name__istartswith=self.q)
      
    return qs
