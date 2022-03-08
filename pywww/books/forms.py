from pyexpat import model
from django import forms

from books.models import Book, Author
from tags.models import Tag

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder

from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple
from dal import autocomplete


'''
class BookForm(forms.ModelForm):
  tags = forms.ModelMultipleChoiceField(
    # Możliwość wyszukiwania tagów i przypisywania ich poza PA
        queryset=Tag.objects.all(),
        # widget=AutocompleteSelectMultiple(
        #   Book._meta.get_field('tags'),
        #   admin.AdminSite()
        # ) Do wyszukiwania tagów bez korzystania z DAL
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete'),
  )
  
  class Meta:
    model = Book
    fields = ('title',
              'description',
              'available',
              'publication_year',
              'authors',
              'tags',
              'image')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = ''
    self.helper.layout = Layout(
      Fieldset(
        'Add Book',
        'title',
        'authors',
        'publication_year',
        'description', 
        'available',
        'tags',
        'image'
      ),
      ButtonHolder(
        Submit('submit', 'Dodaj', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center'
      )
    )
'''  
  
class BookBorrowForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('borrow', 'Wypożycz'))
    
    
class AuthorForm(forms.ModelForm):
  class Meta:
    model = Author
    fields = '__all__'
    
     
class BookForm(forms.ModelForm):
  
  tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
        )
  authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False
        )
  class Meta:
    model = Book
    fields = '__all__'