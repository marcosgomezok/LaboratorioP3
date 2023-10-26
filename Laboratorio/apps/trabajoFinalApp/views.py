from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.trabajoFinalApp.models import Dictamen,Integrante
from apps.persona.models import Alumno
from apps.trabajoFinalApp.forms import ProyectoForm,AlumnoForm,DocenteForm,AsesorForm

def proyecto_lista(request):
    proyectos = Dictamen.objects.get(id=1)#select_related('dictamen_mov__movimiento_proyecto')
    return render(request,'administrador/estadisticas/ptf.html',{'proyectos': proyectos})
                  
# def proyecto_create(request):
#          proyectos = Dictamen.objects.get(id=1)
#          return render(request, "alumno/createPTF.html",
#                   {'proyectos': proyectos})

def proyecto_create(request):
    if request.method == 'POST':

        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        try:
            alumno = Alumno.objects.get(mu=request.POST.get("form_integrante-mu"))
            if form_proyecto.is_valid():
                    proyecto_instance = form_proyecto.save()
                    integrante = Integrante()
                    integrante.alumno = alumno
                    integrante.save()
                    messages.success(request, 'Se ha agregado exitosamente el proyecto')
                    return redirect(reverse('gestion:proyecto_create'))
            else:
                    form_proyecto = ProyectoForm(prefix='form_proyecto')
                    form_integrante = AlumnoForm(prefix='form_integrante')

        except Alumno.DoesNotExist:
            form_integrante = AlumnoForm(prefix='form_integrante')
            messages.error(request, 'Error, Matricula Incorrecta')  
    else:
        form_proyecto = ProyectoForm(prefix='form_proyecto')
        form_integrante = AlumnoForm(prefix='form_integrante')

    return render(request, 'alumno/createPTF.html', {
        'form_proyecto': form_proyecto,
        'form_integrante': form_integrante,
    })

def proyecto_registro(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "registro/registro.html",
                  {'proyectos': proyectos})

def registro_cstf(request):
         proyectos = Dictamen.objects.get(id=1)
         return render(request, "administrador/CSTFs/regCSTF.html",
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
         return render(request, "administrador/estadisticas/estadisticas.html",
                  {'administrador': administrador})

def administrador_alumno_alta(request):
    if request.method == 'POST':

        form_alumno = AlumnoForm(request.POST, prefix='form_alumno')

        if form_alumno.is_valid():
            form_alumno.save()
            form_alumno = AlumnoForm()

    else:
        form_alumno = AlumnoForm( prefix='form_alumno')

    return render(request, "administrador/personas/alumnoAlta.html", {
        'form_alumno': form_alumno,
    })

def administrador_docente_alta(request):
    if request.method == 'POST':

        form_docente = DocenteForm(request.POST, prefix='form_docente')

        if form_docente.is_valid():
            form_docente.save()
            form_docente = DocenteForm()

    else:
        form_docente = DocenteForm( prefix='form_docente')

    return render(request, "administrador/personas/docenteAlta.html", {
        'form_docente': form_docente,
    })

def administrador_asesor_alta(request):
    if request.method == 'POST':

        form_asesor = AsesorForm(request.POST, prefix='form_asesor')

        if form_asesor.is_valid():
            form_asesor.save()
            form_asesor = AsesorForm()

    else:
        form_asesor = AsesorForm( prefix='form_asesor')

    return render(request, "administrador/personas/asesorAlta.html", {
        'form_asesor': form_asesor,
    })
