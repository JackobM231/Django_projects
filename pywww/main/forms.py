from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms



class ContactForm(forms.Form):
  '''Contact form'''
  email = forms.EmailField(label="Adres email")
  title = forms.CharField(label="Tytuł", max_length=255)
  content = forms.CharField(label="Treść", widget=forms.Textarea)
  send_to_me = forms.BooleanField(label="Wyślij do mnie", required=False)
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'contact'
    self.helper.layout = Layout(
      Fieldset(
        'Dane kontaktowe',
        'email',
      ),
      Fieldset(
        'Zawartość',
        'title',
        'content',
      ),
      Fieldset(
        'Dodatkowe',
        HTML('Zaznacz jeśli chcesz otrzymać kopię wiadomość mailem'),
        'send_to_me',
      ),
      ButtonHolder(
        Submit('submit', 'Wyślij', css_class='btn btn-primary'),
        css_class='d-flex justify-content-start'
      )
    )