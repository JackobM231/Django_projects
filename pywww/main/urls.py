from django.urls import path
from main.views import hello_world, about

app_name = 'main'
urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about', about, name='about'),
]