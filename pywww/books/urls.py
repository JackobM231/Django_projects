from django.urls import path
from books.views import books_list, books_table, details

app_name = 'books'
urlpatterns = [
    path('', books_list, name='list'),
    path('table', books_table, name='table'),
    path('<int:book_id>', details, name='details')
]