# from django.shortcuts import render -deleted
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request):
  return render(request, 'main/hello_world.html', {'text': "Hello Word!"})

def about(request):
  return render(request, 'main/about.html')
