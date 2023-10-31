from django import forms
from django.forms import DateInput

from apps.trabajoFinalApp.models import Proyecto
from apps.persona.models import Alumno,Docente,Asesor
from django.contrib.auth.models import User


class ProyectoForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",'rows':1}))
    class Meta:
        model = Proyecto
        fields = ('titulo', 'descripcion','presentacion_ptf')
        widgets = {
            'presentacion_ptf': DateInput(format='%Y-%m-%d', attrs={'type': 'date','required': 'true'}),
        }

class AlumnoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    dni = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    mu = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'dni', 'mu')

class DocenteForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    cuil = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Docente
        fields = ('nombre', 'apellido', 'cuil')

class AsesorForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    cuil = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Asesor
        fields = ('nombre', 'apellido', 'cuil')

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type": "email"}))
    password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","type": "password"}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

