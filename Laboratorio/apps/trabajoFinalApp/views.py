from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# from apps.trabajoFinalApp.forms import PersonaForm, EstadoSaludForm
from apps.trabajoFinalApp.models import Dictamen

def proyecto_lista(request):
    proyectos = Dictamen.objects.get(id=1)#select_related('dictamen_mov__movimiento_proyecto')
    return render(request,'estadisticas\ptf.html',{'proyectos': proyectos})
                  
def proyecto_create(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "ptf\createPTF.html",
                  {'proyectos': proyectos})
