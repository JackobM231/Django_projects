# from django.shortcuts import render -deleted
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book

# Create your views here.
def books_list(request):
  all_books = Book.objects.all()
  books = Book.objects
  context = {'books': all_books, 'unavilable_books': books.filter(available="0"), 'avilable_books': books.filter(available="1")}
  return render(request, 'books/store.html', context)

def books_table(request):
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'books/books_table.html', context)

def details(request, book_id):
  book = Book.objects.get(id=book_id)
  context = {'book': book}
  return render(request, 'books/details.html', context)