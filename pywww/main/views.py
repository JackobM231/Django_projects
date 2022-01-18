# from django.shortcuts import render -deleted
# from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from . import services
from main.forms import ContactForm


# Create your views here.
def hello_world(request):
  return render(request, 'main/hello_world.html', {'text': "Hello Word!"})

def about(request):
  return render(request, 'main/about.html')

def contact(request):
  if request.method == 'POST':
    form = ContactForm(data=request.POST)
    if form.is_valid():
      services.send_message(form.cleaned_data)
      return HttpResponseRedirect(reverse('contact'))
  else:
    form = ContactForm()
    
  return render(request, 'main/contact.html', {'form': form})
