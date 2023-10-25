from django import forms
from django.forms import DateInput

from apps.trabajoFinalApp.models import Proyecto


class ProyectoForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = Proyecto
        fields = ('titulo', 'descripcion')