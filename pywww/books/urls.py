from django.urls import path
from books.views import books_list, books_table, details, add_book_form, edit_book_form, handle_book_borrows

app_name = 'books'
urlpatterns = [
    path('', books_list, name='list'),
    path('add', add_book_form, name='add'),
    path('table', books_table, name='table'),
    path('<int:book_id>/borrows', handle_book_borrows, name='borrows'),
    path('borrows-list/', handle_book_borrows, name='borrows_list'),
    path('<int:book_id>/edit', edit_book_form, name='edit'),
    path('<int:book_id>', details, name='details'),
]