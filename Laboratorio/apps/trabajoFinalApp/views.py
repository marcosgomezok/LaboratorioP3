from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.trabajoFinalApp.models import Dictamen,Integrante,Proyecto
from apps.persona.models import Alumno
from apps.trabajoFinalApp.forms import ProyectoForm,AlumnoForm,DocenteForm,AsesorForm,UserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

def proyecto_lista(request):
    proyectos = User.objects.get(id=1)#select_related('dictamen_mov__movimiento_proyecto')
    return render(request,'administrador/estadisticas/ptf.html',{'proyectos': proyectos})

def proyecto_create(request):
    if request.method == 'POST':

        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        try:
            alumno = Alumno.objects.select_related('user').get(user_id=request.user.id)
            if form_proyecto.is_valid():
                    proyecto_instance = form_proyecto.save()
                    integrante = Integrante()
                    integrante.alumno = alumno
                    integrante.proyecto = proyecto_instance
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
    try:
        alumno = Alumno.objects.select_related('user').get(user_id=request.user.id)
        integrante = Integrante.objects.get(alumno_id=alumno.id)
        proyecto = Proyecto.objects.get(id=integrante.proyecto_id)
        return render(request, 'alumno/estado.html', {
            'proyecto': proyecto,
             })
    except Integrante.DoesNotExist:
        return render(request, 'alumno/createPTF.html', {
                'form_proyecto': form_proyecto,
                'form_integrante': form_integrante,
            })
    #     else:
    #         return render(request, 'alumno/home.html', {
    #             'form_proyecto': form_proyecto,
    #             'form_integrante': form_integrante,
    #         })
    # except Alumno.DoesNotExist:      

def proyecto_registro(request):
         proyectos = User.objects.get(id=1)
         return render(request, "registro/registro.html",
                  {'proyectos': proyectos})

def registro_cstf(request):
         proyectos = User.objects.get(id=1)
         return render(request, "administrador/CSTFs/regCSTF.html",
                  {'proyectos': proyectos})

def proyecto_evaluacion_cstf(request):
         proyectos = User.objects.get(id=1)
         return render(request, "cstf/evaluacion.html",
                  {'proyectos': proyectos})

def alumno(request):
         alumnos = User.objects.get(id=1)
         return render(request, "alumno/home.html",
                  {'alumnos': alumnos})

def cstf(request):
         cstf = User.objects.get(id=1)
         return render(request, "cstf/home.html",
                  {'cstf': cstf})
def cstf_evaluacion(request):
         cstf = User.objects.get(id=1)
         return render(request, "cstf/evaluacion.html",
                  {'cstf': cstf})

def tribunal(request):
         tribunal = User.objects.get(id=1)
         return render(request, "tribunal/home.html",
                  {'tribunal': tribunal})

def administrador(request):
         administrador = User.objects.get(id=1)
         return render(request, "administrador/home.html",
                  {'administrador': administrador})

def administrador_estadisticas(request):
         administrador = User.objects.get(id=1)
         return render(request, "administrador/estadisticas/estadisticas.html",
                  {'administrador': administrador})

def administrador_alumno_alta(request):
    if request.method == 'POST':

        form_alumno = AlumnoForm(request.POST, prefix='form_alumno')
        form_user = UserForm(request.POST, prefix='form_user')

        if form_alumno.is_valid():
            temp_user = form_user.save(commit=False)
            alumno = form_alumno.save(commit=False)
            user = User.objects.create_user(temp_user.username, temp_user.email, temp_user.password)
            user.save()
            group = Group.objects.get(name='Alumno')
            user.groups.add(group)
            alumno.user = user
            alumno.save()
            form_alumno = AlumnoForm()
            form_user = UserForm()

    else:
        form_alumno = AlumnoForm( prefix='form_alumno')
        form_user = UserForm( prefix='form_user')

    return render(request, "administrador/personas/alumnoAlta.html", {
        'form_alumno': form_alumno,
        'form_user': form_user,
    })

def administrador_docente_alta(request):
    if request.method == 'POST':

        form_docente = DocenteForm(request.POST, prefix='form_docente')
        form_user = UserForm(request.POST, prefix='form_user')

        if form_docente.is_valid():
            temp_user = form_user.save(commit=False)
            docente = form_docente.save(commit=False)
            user = User.objects.create_user(temp_user.username, temp_user.email, temp_user.password)
            user.save()
            group = Group.objects.get(name=request.POST.get("form_docente-rol"))
            user.groups.add(group)
            docente.user = user
            docente.save()
            form_docente = DocenteForm()
            form_user = UserForm()


    else:
        form_docente = DocenteForm( prefix='form_docente')
        form_user = UserForm( prefix='form_user')

    return render(request, "administrador/personas/docenteAlta.html", {
        'form_docente': form_docente,
        'form_user': form_user,
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
