from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def login(request):
    login = AuthenticationForm()
    return render(request, 'login.html', {'login':login})

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form':form})