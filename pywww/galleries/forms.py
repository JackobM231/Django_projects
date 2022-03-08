from django import forms

from .models import Gallery, Photo

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder



class AddGalleryForm(forms.ModelForm):
  # status = forms.ChoiceField(
  #     ('NEW', 'new'),
  #     ('PUBLISHED', 'published'),
  #     ('HIDE', 'hide'),
  #   )
  
  class Meta:
    model = Gallery
    fields = ['title', 'description', 'status']
    labels = {
      'title': 'Tytuł',
      'description': 'Opis',
      'status': 'Status'
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method= 'POST'
    self.helper.layout = Layout(
      Fieldset(
        'Dodaj nową galerię',
        'title',
        'description',
        'status'
      ),
      ButtonHolder(
        Submit('submit', 'Zapisz', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center'
      )     
    )
    
    
class AddGalleryPhotoForm(forms.ModelForm):

  class Meta:
    model = Photo
    fields = ['title', 'short_description', 'image', 'source', 'status']
    labels = {
      'title': 'Tytuł',
      'short_description': 'Opis',
      'image': 'Zdjęcie/Obraz',
      'source': 'Źródło',
      'status': 'Status'
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method= 'POST'
    self.helper.layout = Layout(
      Fieldset(
        'Dodaj zdjęcie do galerii',
        'title',
        'short_description',
        'image',
        'source',
        'status'
      ),
      ButtonHolder(
        Submit('submit', 'Dodaj', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center'
      )     
    )