from dataclasses import fields
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
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
  
  
class BookBorrowForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.add_input(Submit('borrow', 'Wypożycz'))