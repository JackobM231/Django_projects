from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div
from django import forms
from posts.models import Post


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
  class Meta:
    model = Post
    fields = ('title', 'content', 'published', 'sponsored')
    labels = {
      'title': 'Tytuł',
      'content': 'Treść',
      'published': 'Opublikowany',
      'sponsored': 'Sponsorowany'
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
        'published', 
        'sponsored'
      ),
      ButtonHolder(
        Submit('submit', 'Dodaj', css_class='btn btn-primary'),
        css_class='d-flex justify-content-center'
      )
    )