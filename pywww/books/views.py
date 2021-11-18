# from django.shortcuts import render -deleted
from django.http import HttpResponse

# Create your views here.
def books_list(request):
  return HttpResponse("Tu będzie moja biblioteka")
