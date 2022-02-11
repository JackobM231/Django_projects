from django.urls import path

from .views import TagAutocomplete

app_name = 'tags'
urlpatterns = [
  path('tag-autocomplete/', TagAutocomplete.as_view(create_field='name'), name='tag-autocomplete'),
  # create_field='name' pozwala dodwać nowe tagi w trakcie dodawania posta na stronie poza PA
]