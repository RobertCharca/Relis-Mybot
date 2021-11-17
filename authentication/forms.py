from django.db.models import fields
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from authentication.models import Alumnos

class CreateUserForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = "__all__"
        labels = {
            'id_alumno': '',
            'apellidos': '',
            'nombre': '',
            'edad': '',
            'celular': '',
            'dni': '',
            'direccion': '',
            'cod_carrera': '',
            'correo_alumno': '',
            'password_alumno': ''
        }
        widgets = {
            'id_alumno': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Id de alumno'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'edad': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Edad'}),
            'celular': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de celular (o teléfono)'}),
            'dni': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'DNI'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'cod_carrera': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código de la carrera'}),
            'correo_alumno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}),
            'password_alumno': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contraseña'})
        }