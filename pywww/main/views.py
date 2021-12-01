# from django.shortcuts import render -deleted
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_word(request):
  return render(request, 'main/about.html', {'text': "Hello Word!"})
