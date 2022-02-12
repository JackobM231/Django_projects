# from django.shortcuts import render -deleted
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from books.models import Book, Borrow
from books.forms import BookForm, BookBorrowForm


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
  form = BookBorrowForm()
  form.helper.form_action = reverse('books:borrows', args=[book.id])
  context = {
            'book': book,
            'form': form
             }
  return render(request, 'books/details.html', context)


def add_book_form(request):
  if request.method == 'POST' and request.user.is_authenticated:
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      form.save_m2m()
      # Zapis elementów powiązanych m2m z book
      return HttpResponseRedirect(reverse('books:add'))
  else:
    form = BookForm()

  return render(request, 'books/add_book.html', {'form': form})


def edit_book_form(request, book_id):
  book = get_object_or_404(Book, id=book_id)
  if request.method == 'POST' and request.user.is_authenticated:
    form = BookForm(request.POST, request.FILES, instance=book)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('books:details', args=[book_id]))
  else:
    form = BookForm(instance=book)
      
  return render(request, 'books/add_book.html', {'form': form})


def handle_book_borrows(request, book_id=None):
  # Po wejściu z details
  user = request.user
  if user.is_authenticated:
    if request.method == 'POST':
    # Po kliknięciu wypożycz w details
      if request.POST.get('borrow'):
        book = Book.objects.get(pk=book_id)
        Borrow.objects.create(
          user = user, 
          book = book
        )
        book.available = False
        book.save()
        return HttpResponseRedirect(reverse('books:details', args=[book_id]))
      else:
        keys = [key for key in request.POST.keys() if key.startswith('book_')]
        key = int(keys[0].split('_')[1])
        book = Book.objects.get(id=key)
        borrow = Borrow.objects.filter(user=user, book=book).last()
        # Ostatnia z wypożyczonych książek
        if not borrow.return_date:
          borrow.return_date = timezone.now()
          borrow.save()
          book.available = True
          book.save()
        return HttpResponseRedirect(reverse('books:borrows_list'))     
    else:
      borrows = Borrow.objects.filter(user=user)
      return render(request, 'books/borrows_list.html', {'borrows': borrows})
  else:
     return HttpResponseRedirect(reverse('books:list'))   
    