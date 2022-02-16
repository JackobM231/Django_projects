from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import RegisterForm

# Create your views here.

def register(response):
  if response.method == 'POST':
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
    return render(response, 'registration/login.html', {'context': 'Registration was successful'})   
  else:
    form = RegisterForm()
  return render(response, 'accounts/register.html', {'form': form})
  
def login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    # Redirection to success page
  else:
    # Redirection to fail page
    pass