from django.urls import path
from books.views import books_list, books_table

urlpatterns = [
    path('', books_list),
    path('1', books_table),
]