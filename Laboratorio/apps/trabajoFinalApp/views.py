from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.trabajoFinalApp.models import Dictamen,Integrante,Proyecto,Movimiento,Cstf,Miembro_Cstf,Tribunal,Miembro_Titular,Miembro_Suplente
from apps.persona.models import Alumno,Docente,Asesor
from apps.trabajoFinalApp.forms import ProyectoForm,AlumnoForm,DocenteForm,AsesorForm,UserForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

def proyecto_lista(request):
    proyectos = Proyecto.objects.all()
    return render(request,'administrador/estadisticas/ptf.html',{'proyectos': proyectos})

def proyecto_integrante(request):
    #obtengo el proyecto asignado al usuario logeado
    alumno = Alumno.objects.select_related('user').filter(user_id=request.user.id).first()
    integrante = Integrante.objects.filter(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=False).first()
    if integrante is not None:
        proyecto = Proyecto.objects.filter(id=integrante.proyecto_id).first()

    #NO HAY un proyecto asignado al usuario:
    else:
        return redirect(reverse('gestion:proyecto_create'))
         
    if request.method == 'POST':
        try:
            #asigno el alumno a un nuevo registro de integrantes
            alumno = Alumno.objects.select_related('user').get(mu=request.POST.get("integrante-mu"))

            integrante = Integrante.objects.filter(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=True).first()
            if(integrante is not None):
                 integrante.alumno = alumno
                 integrante.proyecto = proyecto
                 integrante.alta_proyecto =datetime.now()
                 integrante.save()
            else:
                 messages.error(request, 'Error, Matricula Incorrecta')     
        except Alumno.DoesNotExist:
            messages.error(request, 'Error, Matricula Incorrecta')
            return render(request, 'alumno/integrante.html')
    return render(request, 'alumno/integrante.html')

def proyecto_baja(request):

    alumno = Alumno.objects.select_related('user').filter(user_id=request.user.id).first()
    integrante = Integrante.objects.filter(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=False).first()
    
    if integrante is not None:
        proyecto = Proyecto.objects.filter(id=integrante.proyecto_id).first()
        if request.method == 'POST':
            integrante.baja_proyecto=datetime.now()
            integrante.save()
            new = Integrante()
            new.alumno=alumno
            new.save()
            return render(request, 'alumno/home.html')
        return render(request, 'alumno/baja.html', {
                     'proyecto': proyecto,
                     })
    else:
         return redirect(reverse('gestion:proyecto_create'))
    
def proyecto_entrega(request):

    alumno = Alumno.objects.select_related('user').filter(user_id=request.user.id).first()
    integrante = Integrante.objects.filter(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=False).first()
    if integrante is not None:
        proyecto = Proyecto.objects.filter(id=integrante.proyecto_id).first()
        dictamen = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__id=proyecto.id).last()
        
        if request.method == 'POST':
            if dictamen is None:
                dictamen = Dictamen()
                movimiento = Movimiento()
                movimiento.tipo_mov = 'proyecto_presentado'
                movimiento.fecha_mov =datetime.now()
                movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                movimiento.movimiento_proyecto=proyecto
                movimiento.save()
                dictamen.dictamen_mov=movimiento
                dictamen.resultado_dictamen='aceptado'
                dictamen.save()
            else:
                if(dictamen.dictamen_mov.tipo_mov == 'proyecto_presentado'):
                    if(dictamen.resultado_dictamen == 'aceptado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_cstf'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                if(dictamen.dictamen_mov.tipo_mov == 'evaluacion_cstf'):
                    if(dictamen.resultado_dictamen == 'aceptado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_tribunal'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                    if(dictamen.resultado_dictamen == 'rechazado' or dictamen.resultado_dictamen == 'observado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_cstf'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                if(dictamen.dictamen_mov.tipo_mov == 'evaluacion_tribunal'):
                    if(dictamen.resultado_dictamen == 'aceptado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_borrador'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                    if(dictamen.resultado_dictamen == 'rechazado' or dictamen.resultado_dictamen == 'observado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_tribunal'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                if(dictamen.dictamen_mov.tipo_mov == 'evaluacion_borrador'):
                    if(dictamen.resultado_dictamen == 'aceptado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_final'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                    if(dictamen.resultado_dictamen == 'rechazado' or dictamen.resultado_dictamen == 'observado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_borrador'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                if(dictamen.dictamen_mov.tipo_mov == 'evaluacion_final'):
                    if(dictamen.resultado_dictamen == 'rechazado' or dictamen.resultado_dictamen == 'observado'):
                        dictamen = Dictamen()
                        movimiento = Movimiento()
                        movimiento.tipo_mov = 'evaluacion_final'
                        movimiento.fecha_mov =datetime.now()
                        movimiento.fin_mov =datetime.now().replace(year=datetime.now().year + 1)
                        movimiento.movimiento_proyecto=proyecto
                        movimiento.save()
                        dictamen.dictamen_mov=movimiento
                        dictamen.save()
                          
                return render(request, 'alumno/entrega.html', {
                     'proyecto': proyecto,
                     'dictamen':dictamen,
                     })
        return render(request, 'alumno/entrega.html', {
                     'proyecto': proyecto,
                     'dictamen':dictamen,
                     })
    else:
         return redirect(reverse('gestion:proyecto_create'))


def proyecto_create(request):
    if request.method == 'POST':

        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        try:
            alumno = Alumno.objects.select_related('user').get(user_id=request.user.id)
            if form_proyecto.is_valid():
                    proyecto_instance = form_proyecto.save()
                    proyecto_instance.cstf_proyecto = Cstf.objects.first()
                    proyecto_instance.tribunal_proyecto = Tribunal.objects.first()
                    proyecto_instance.save()
                    integrante = Integrante.objects.filter(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=True).first()
                    integrante.alta_proyecto =datetime.now()
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
        integrante = Integrante.objects.get(alumno_id=alumno.id,baja_proyecto=None,alta_proyecto__isnull=False)
        proyecto = Proyecto.objects.get(id=integrante.proyecto_id)
        return render(request, 'alumno/estado.html', {
            'proyecto': proyecto,
             })
    except Integrante.DoesNotExist:
        return render(request, 'alumno/createPTF.html', {
                'form_proyecto': form_proyecto,
                'form_integrante': form_integrante,
            })
   

def administrador_proyecto_alta(request):

    alumnos = Integrante.objects.select_related('alumno').filter(alta_proyecto=None)
    tribunales = Tribunal.objects.all()
    comisiones = Cstf.objects.all()
    docentes = Docente.objects.all()
    asesores = Asesor.objects.all()

    if request.method == 'POST':
        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        if form_proyecto.is_valid():
                    alumno = Alumno.objects.get(id=request.POST.get("alumno-id"))
                    tribunal = Tribunal.objects.get(id=request.POST.get("tribunal-id"))
                    comision = Cstf.objects.get(id=request.POST.get("comision-id"))
                    asesor = Asesor.objects.get(id=request.POST.get("asesor-id"))
                    director = Docente.objects.get(id=request.POST.get("director-id"))
                    codirector = Docente.objects.get(id=request.POST.get("co-director-id"))

                    proyecto_instance = form_proyecto.save()
                    proyecto_instance.cstf_proyecto = comision
                    proyecto_instance.tribunal_proyecto = tribunal
                    proyecto_instance.director = director
                    proyecto_instance.co_director = codirector
                    proyecto_instance.asesor = asesor
                    proyecto_instance.save()
                    integrante_temp = Integrante.objects.select_related('alumno').filter(alumno__id=alumno.id,alta_proyecto=None).first()
                    integrante = Integrante.objects.get(id=integrante_temp.id)

                    integrante.alta_proyecto =datetime.now()
                    integrante.alumno = alumno
                    integrante.proyecto = proyecto_instance
                    integrante.save()
                    messages.success(request, 'Se ha agregado exitosamente el proyecto')
                    return redirect(reverse('gestion:administrador_proyecto_alta'))
        else:
            form_proyecto = ProyectoForm(prefix='form_proyecto')

    else:    
        form_proyecto = ProyectoForm(prefix='form_proyecto')

    return render(request, "administrador/proyecto/alta.html", 
                  {'form_proyecto': form_proyecto,'tribunales':tribunales,'comisiones':comisiones ,'alumnos':alumnos,'docentes':docentes,'asesores':asesores})

def administrador_proyecto_modificar(request):

    tribunales = Tribunal.objects.all()
    comisiones = Cstf.objects.all()
    docentes = Docente.objects.all()
    asesores = Asesor.objects.all()
    proyectos = Proyecto.objects.all()
    editar = None

    if request.method == 'POST':
        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        editar = Proyecto.objects.filter(id=request.POST.get("proyecto-id")).first()
        if 'actualizar' in request.POST: 
            if form_proyecto.is_valid():
                        editar = Proyecto.objects.filter(id=request.POST.get("proyecto-id-2")).first()
                        tribunal = Tribunal.objects.get(id=request.POST.get("tribunal-id"))
                        comision = Cstf.objects.get(id=request.POST.get("comision-id"))
                        asesor = Asesor.objects.get(id=request.POST.get("asesor-id"))
                        director = Docente.objects.get(id=request.POST.get("director-id"))
                        codirector = Docente.objects.get(id=request.POST.get("co-director-id"))
                        editar.cstf_proyecto = comision
                        editar.tribunal_proyecto = tribunal
                        editar.director = director
                        editar.co_director = codirector
                        editar.asesor = asesor
                        temp = form_proyecto.save(commit=False)
                        editar.titulo= temp.titulo
                        editar.descripcion= temp.descripcion
                        editar.presentacion_ptf= temp.presentacion_ptf
                        editar.save()
                        return redirect(reverse('gestion:administrador_proyecto_modificar'))
            else:
                form_proyecto = ProyectoForm(prefix='form_proyecto')
        if 'buscar' in request.POST:
             
             return render(request, "administrador/proyecto/modificar.html", 
                           {'form_proyecto': form_proyecto,'tribunales':tribunales,'comisiones':comisiones ,'docentes':docentes,'asesores':asesores,'proyectos':proyectos,'editar':editar})

    else:   
        form_proyecto = ProyectoForm(prefix='form_proyecto')

    return render(request, "administrador/proyecto/modificar.html", 
                  {'form_proyecto': form_proyecto,'tribunales':tribunales,'comisiones':comisiones ,'docentes':docentes,'asesores':asesores,'proyectos':proyectos,'editar':editar})
    

def administrador_integrante_alumno(request):
    
    editar = None
    alumnos = Integrante.objects.select_related('alumno').filter(alta_proyecto=None)
    proyectos = Proyecto.objects.all()

    if request.method == 'POST':
        form_proyecto = ProyectoForm(request.POST, prefix='form_proyecto')
        editar = Proyecto.objects.filter(id=request.POST.get("proyecto-id")).first()
        if 'actualizar' in request.POST: 
            
                    editar = Proyecto.objects.filter(id=request.POST.get("proyecto-id-2")).first()
                    integrante = Integrante.objects.filter(alumno_id=request.POST.get("alumno-id"),alta_proyecto=None).first()
                    integrante.proyecto = editar
                    integrante.alta_proyecto =datetime.now()
                    integrante.save()
                    return redirect(reverse('gestion:administrador_integrante_alumno'))

        if 'buscar' in request.POST:
             
             return render(request, "administrador/integrantes/alumno.html", 
                           {'form_proyecto': form_proyecto,'proyectos':proyectos,'editar':editar,'alumnos':alumnos})

    else:    
        form_proyecto = ProyectoForm(prefix='form_proyecto')

    return render(request, "administrador/integrantes/alumno.html", 
                  {'form_proyecto': form_proyecto,'proyectos':proyectos,'editar':editar,'alumnos':alumnos})
    
def alumno(request):
         return render(request, "alumno/home.html")

def docente(request):
         return render(request, "docente/home.html")

def cstf(request):
         return render(request, "cstf/home.html")

def cstf_evaluacion(request):
        docente = Docente.objects.select_related('user').filter(user=request.user.id).first()
        miembro = Miembro_Cstf.objects.filter(docente=docente.id).first()
        dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__cstf_proyecto=miembro.comision_cstf,dictamen_mov__tipo_mov='evaluacion_cstf',resultado_dictamen=None)
        if request.method == 'POST':   
            editar = dictamenes.filter(id=request.POST.get("proyecto-id")).first()

            if 'guardar-edicion' in request.POST: 
                editar = dictamenes.filter(id=request.POST.get("proyecto-id-2")).first()

                editar.resultado_dictamen = request.POST.get("resultado_dictamen")
                editar.observacion = request.POST.get("observacion")
                editar.save()

                editar = None
            if 'cancelar-edicion' in request.POST: 
                  editar = None
            return render(request, "cstf/evaluacion.html",{'dictamenes': dictamenes,'editar':editar})
        return render(request, "cstf/evaluacion.html",{'dictamenes': dictamenes})

def tribunal(request):
         return render(request, "tribunal/home.html")

def tribunal_evaluacion_ptf(request):
         docente = Docente.objects.select_related('user').filter(user=request.user.id).first()
         miembro = Miembro_Titular.objects.filter(vocal_titular=docente.id).first()
         if(miembro is not None):
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_mt,dictamen_mov__tipo_mov='evaluacion_tribunal',resultado_dictamen=None)
         else:  
            miembro = Miembro_Suplente.objects.filter(vocal_suplente=docente.id).first()
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_ms,dictamen_mov__tipo_mov='evaluacion_tribunal',resultado_dictamen=None)
         if request.method == 'POST':   
            editar = dictamenes.filter(id=request.POST.get("proyecto-id")).first()

            if 'guardar-edicion' in request.POST: 
                editar = dictamenes.filter(id=request.POST.get("proyecto-id-2")).first()

                editar.resultado_dictamen = request.POST.get("resultado_dictamen")
                editar.observacion = request.POST.get("observacion")
                editar.save()

                editar = None
            if 'cancelar-edicion' in request.POST: 
                  editar = None
            return render(request, "tribunal/evaluacionPTF.html",{'dictamenes': dictamenes,'editar':editar})
         return render(request, "tribunal/evaluacionPTF.html",{'dictamenes': dictamenes})

def tribunal_evaluacion_borrador(request):
         docente = Docente.objects.select_related('user').filter(user=request.user.id).first()
         miembro = Miembro_Titular.objects.filter(vocal_titular=docente.id).first()
         if(miembro is not None):
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_mt,dictamen_mov__tipo_mov='evaluacion_borrador',resultado_dictamen=None)
         else:  
            miembro = Miembro_Suplente.objects.filter(vocal_suplente=docente.id).first()
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_ms,dictamen_mov__tipo_mov='evaluacion_borrador',resultado_dictamen=None)
         if request.method == 'POST':   
            editar = dictamenes.filter(id=request.POST.get("proyecto-id")).first()

            if 'guardar-edicion' in request.POST: 
                editar = dictamenes.filter(id=request.POST.get("proyecto-id-2")).first()

                editar.resultado_dictamen = request.POST.get("resultado_dictamen")
                editar.observacion = request.POST.get("observacion")
                editar.save()

                editar = None
            if 'cancelar-edicion' in request.POST: 
                  editar = None
            return render(request, "tribunal/evaluacionBTF.html",{'dictamenes': dictamenes,'editar':editar})
         return render(request, "tribunal/evaluacionBTF.html",{'dictamenes': dictamenes})

def tribunal_evaluacion_final(request):
         docente = Docente.objects.select_related('user').filter(user=request.user.id).first()
         miembro = Miembro_Titular.objects.filter(vocal_titular=docente.id).first()
         if(miembro is not None):
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_mt,dictamen_mov__tipo_mov='evaluacion_final',resultado_dictamen=None)
         else:  
            miembro = Miembro_Suplente.objects.filter(vocal_suplente=docente.id).first()
            dictamenes = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__tribunal_proyecto=miembro.tribunal_ms,dictamen_mov__tipo_mov='evaluacion_final',resultado_dictamen=None)
         if request.method == 'POST':   
            editar = dictamenes.filter(id=request.POST.get("proyecto-id")).first()

            if 'guardar-edicion' in request.POST: 
                editar = dictamenes.filter(id=request.POST.get("proyecto-id-2")).first()

                editar.resultado_dictamen = request.POST.get("resultado_dictamen")
                editar.observacion = request.POST.get("observacion")
                editar.save()

                editar = None
            if 'cancelar-edicion' in request.POST: 
                  editar = None
            return render(request, "tribunal/evaluacionFINAL.html",{'dictamenes': dictamenes,'editar':editar})
         return render(request, "tribunal/evaluacionFINAL.html",{'dictamenes': dictamenes})

def registro_cstf(request):
        try:
            comisiones = Cstf.objects.all()
            docentes = Docente.objects.select_related('docente','vocal_suplente','vocal_titular').filter(docente__docente_id=None,vocal_titular__vocal_titular_id=None,vocal_suplente__vocal_suplente_id=None)
            if request.method=='POST':
                if 'agregar-comision' in request.POST:    
                    cstf = Cstf(fecha_creacion=datetime.now())
                    cstf.save() 
                    return render(request, "administrador/CSTFs/regCSTF.html",{'comisiones':comisiones,'docentes':docentes})
            if request.method=='POST':
                if 'agregar-miembro' in request.POST: 
                    docente = Docente.objects.filter(id=request.POST.get("docente-id")).first()
                    comision = Cstf.objects.filter(id=request.POST.get("comision-id")).first()
                    miembro = Miembro_Cstf()
                    miembro.docente = docente
                    miembro.comision_cstf = comision
                    miembro.save()
                    group = Group.objects.get(name='CSTF')
                    docente.user.groups.add(group)
            return render(request, "administrador/CSTFs/regCSTF.html",{'comisiones':comisiones,'docentes':docentes})
        except Cstf.DoesNotExist:
            return render(request, "administrador/CSTFs/regCSTF.html")
        
def tribunal_nuevo(request):
        try:
            tribunales = Tribunal.objects.all()
            docentes = Docente.objects.select_related('docente','vocal_suplente','vocal_titular').filter(docente__docente_id=None,vocal_titular__vocal_titular_id=None,vocal_suplente__vocal_suplente_id=None)
            if request.method=='POST':
                if 'agregar-tribunal' in request.POST:    
                    tribunal = Tribunal()
                    tribunal.disposicion = datetime.now()
                    tribunal.presidente = Docente.objects.filter(id=request.POST.get("director-id")).first()
                    tribunal.save() 
                    tribunal.nro_disposicion=tribunal.id
                    tribunal.save() 
                    return render(request, "administrador/tribunales/alta.html",{'tribunales':tribunales,'docentes':docentes})
            if request.method=='POST':
                if 'agregar-miembro' in request.POST: 
                    docente = Docente.objects.filter(id=request.POST.get("docente-id")).first()
                    tribunal = Tribunal.objects.filter(id=request.POST.get("tribunal-id")).first()
                    if(request.POST.get("form_docente-rol")=='titular'):
                        miembro = Miembro_Titular()
                        miembro.tribunal_mt = tribunal
                        miembro.vocal_titular = docente
                    else:
                        miembro = Miembro_Suplente()
                        miembro.tribunal_ms = tribunal
                        miembro.vocal_suplente = docente
                    miembro.save()
                    group = Group.objects.get(name='Tribunal')
                    docente.user.groups.add(group)
            return render(request, "administrador/tribunales/alta.html",{'tribunales':tribunales,'docentes':docentes})
        except Tribunal.DoesNotExist:
            return render(request, "administrador/tribunales/alta.html")

def administrador(request):
         return render(request, "administrador/home.html")

def administrador_estadisticas(request):
         return render(request, "administrador/estadisticas/estadisticas.html")

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
            integrante = Integrante()
            integrante.alumno = alumno
            integrante.save()

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
        form_user = UserForm(request.POST, prefix='form_user')

        if form_asesor.is_valid():

            temp_user = form_user.save(commit=False)
            asesor = form_asesor.save(commit=False)
            user = User.objects.create_user(temp_user.username, temp_user.email, temp_user.password)
            user.save()

            asesor.user = user
            asesor.save()
            form_asesor = AsesorForm()
            form_user = UserForm()
    else:
        form_asesor = AsesorForm( prefix='form_asesor')
        form_user = UserForm( prefix='form_user')

    return render(request, "administrador/personas/asesorAlta.html", {
        'form_asesor': form_asesor,
        'form_user': form_user,
    })
