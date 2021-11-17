from django.db.models.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se registró correctamente el alumno')
            return redirect('relis')
    return render(request, 'register.html', {'form':form})

def loginStudent(request):
    if request.method == "POST":
        user_email = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(request, id=user_email, password=user_password)
        print('USER:', user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/relis')
        else:
            messages.info(request, 'El nombre o contraseña son incorrectos')
    return render(request, 'login.html', {})

def logoutStudent(request):
    logout(request)
    return redirect('login')

def relis_page(request):
    return render(request, 'relis_chatbot.html', {})