from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# from apps.trabajoFinalApp.forms import PersonaForm, EstadoSaludForm
from apps.trabajoFinalApp.models import Dictamen

def proyecto_lista(request):
    proyectos = Dictamen.objects.get(id=1)#select_related('dictamen_mov__movimiento_proyecto')
    return render(request,'estadisticas/ptf.html',{'proyectos': proyectos})
                  
def proyecto_create(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "ptf/createPTF.html",
                  {'proyectos': proyectos})

def proyecto_registro(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "registro/registro.html",
                  {'proyectos': proyectos})

def registro_cstf(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "cstf/regCSTF.html",
                  {'proyectos': proyectos})

def proyecto_evaluacion_cstf(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "cstf/evaluacion.html",
                  {'proyectos': proyectos})

def alumno(request):
         alumnos = Dictamen.objects.get(id=1)
         return render(request, "alumno/home.html",
                  {'alumnos': alumnos})

def cstf(request):
         cstf = Dictamen.objects.get(id=1)
         return render(request, "cstf/home.html",
                  {'cstf': cstf})
def cstf_evaluacion(request):
         cstf = Dictamen.objects.get(id=1)
         return render(request, "cstf/evaluacion.html",
                  {'cstf': cstf})

def tribunal(request):
         tribunal = Dictamen.objects.get(id=1)
         return render(request, "tribunal/home.html",
                  {'tribunal': tribunal})

def administrador(request):
         administrador = Dictamen.objects.get(id=1)
         return render(request, "administrador/home.html",
                  {'administrador': administrador})

def administrador_estadisticas(request):
         administrador = Dictamen.objects.get(id=1)
         return render(request, "estadisticas/estadisticas.html",
                  {'administrador': administrador})
