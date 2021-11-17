from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.

def login(request):
    login = AuthenticationForm()
    return render(request, 'login.html', {'login':login})

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se registró correctamente el alumno')
    return render(request, 'register.html', {'form':form})