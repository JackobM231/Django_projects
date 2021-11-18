# from django.shortcuts import render -deleted
from django.http import HttpResponse

def hello_word(request):
  return HttpResponse("Hello Word!")

# Create your views here.
