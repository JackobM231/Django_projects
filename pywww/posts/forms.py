from django import forms
from dal import autocomplete

from posts.models import Post
from tags.models import Tag

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div

from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple


# class PostForm(forms.Form):
#   '''Add new post form'''
#   title = forms.CharField(label="Tytuł", max_length=255)
#   content = forms.CharField(label="Treść", widget=forms.Textarea)
#   published = forms.BooleanField(label="Publiczny", required=False)
#   sponsored = forms.BooleanField(label="Sponsorowany", required=False)
  
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.helper = FormHelper()
#     self.helper.form_method = 'post'
#     self.helper.form_action = 'add'
#     self.helper.layout = Layout(
#       Div (
#         Fieldset(
#           'Dodaj nowy post',
#           'title',
#           'content',
#           'published',
#           'sponsored',
#           css_class='crispy_forms col-md-6'
#         ),
#         ButtonHolder(
#           Submit('submit', 'Dodaj', css_class='btn btn-primary'),
#           css_class='d-flex justify-content-center'
#         ),
#         css_class='row justify-content-md-center',  
#       )
#     )

class PostForm(forms.ModelForm):
  tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget = autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete') 
        # widget=AutocompleteSelectMultiple(
        #       Post._meta.get_field('tags'),
        #       admin.AdminSite(),
        # ) Do wyszukiwania bez DAL
  )
  
  class Meta:
    model = Post
    fields = ['title', 'content', 'published', 'sponsored', 'image', 'tags']
    labels = {
      'title': 'Tytuł',
      'content': 'Treść',
      'published': 'Opublikowany',
      'sponsored': 'Sponsorowany',
      'iamge': 'Obraz',
      'tags' : 'Tagi',
    }
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = ''
    self.helper.layout = Layout(
      Fieldset(
        'Dodaj post',
        'title',
        'content',
        'tags',
        'image',
        'published', 
        'sponsored',
      ),
      ButtonHolder(
        Submit('submit', 'Zapisz', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center'
      )
    )