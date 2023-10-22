from django.db import models

from apps.persona.models import Docente,Alumno,Asesor
# Create your models here.

class Cstf(models.Model):
    fecha_creacion = models.DateField(null=True, blank=True)

class Miembro_Cstf(models.Model):
    comision_cstf = models.ForeignKey(Cstf, on_delete=models.CASCADE,null=True, blank=True,related_name='comision')
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE,null=True, blank=True,related_name='docente')

class Tribunal(models.Model):
    
    disposicion = models.DateField(null=True, blank=True)
    nro_disposicion = models.CharField(null=True, blank=True)
    archivo_tribunal = models.FileField(null=True)
    presidente = models.OneToOneField(Docente, on_delete=models.SET_NULL,null=True, blank=True)

class Miembro_Titular(models.Model):
    tribunal_mt = models.ForeignKey(Tribunal, on_delete=models.CASCADE,null=True, blank=True,related_name='tribunal_mt')
    vocal_titular = models.OneToOneField(Docente, on_delete=models.CASCADE,null=True, blank=True,related_name='vocal_titular')

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=2000)
    presentacion_ptf = models.DateField(null=True, blank=True)
    nota_aceptacion_director = models.FileField(null=True)
    director = models.OneToOneField(Docente, on_delete=models.SET_NULL,null=True, blank=True,related_name='director')
    co_director = models.OneToOneField(Docente, on_delete=models.SET_NULL,null=True, blank=True,related_name='co_director')
    asesor = models.OneToOneField(Asesor, on_delete=models.SET_NULL,null=True, blank=True,related_name='asesor')
    cstf_proyecto = models.OneToOneField(Cstf, on_delete=models.CASCADE,null=True, blank=True,related_name='cstf_proyecto')
    tribunal_proyecto = models.OneToOneField(Tribunal, on_delete=models.CASCADE,null=True, blank=True,related_name='tribunal_proyecto')

class Miembro_Suplente(models.Model):
    tribunal_ms = models.ForeignKey(Tribunal, on_delete=models.CASCADE,null=True, blank=True,related_name='tribunal_ms')
    vocal_suplente = models.OneToOneField(Docente, on_delete=models.CASCADE,null=True, blank=True,related_name='vocal_suplente')

class RegistroDirector(models.Model):
    alta_proyecto = models.DateField(null=True, blank=True)
    baja_proyecto = models.DateField(null=True, blank=True)
    director = models.OneToOneField(Docente, on_delete=models.CASCADE,null=True, blank=True,related_name='director_registro')
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE,null=True, blank=True,related_name='director_proyecto')

class Integrante(models.Model):
    alta_proyecto = models.DateField(null=True, blank=True)
    baja_proyecto = models.DateField(null=True, blank=True)
    analitico = models.FileField(null=True, blank=True)
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE,null=True, blank=True,related_name='integrante_alumno')
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE,null=True, blank=True,related_name='integrante_proyecto')

class Movimiento(models.Model):
    MOVIMIENTO_OPCIONES = (
        ('proyecto_presentado', 'Proyecto Presentado'),
        ('evaluacion_cstf', 'Proyecto en Evaluación por CSTF'),
        ('evaluacion_tribunal', 'Proyecto en Evaluación por Tribunal'),
        ('evaluacion_borrador', 'Borrador en Evaluación por el Tribunal'),
        ('evaluacion_final', 'Defensa del Trabajo Final'),
    )
    movimiento_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null=True, blank=True,related_name='movimiento_proyecto')
    fecha_mov = models.DateField(null=True, blank=True)
    fin_mov = models.DateField(null=True, blank=True)
    tipo_mov = models.CharField(max_length=200,null=True, blank=True, choices=MOVIMIENTO_OPCIONES)

class ArchivosTF(models.Model):
    archivos_tf = models.FileField(null=True, blank=True)
    archivo_mov = models.OneToOneField(Movimiento, on_delete=models.CASCADE,null=True, blank=True,related_name='archivo_mov')

class Dictamen(models.Model):
    DICTAMEN_OPCIONES = (
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
        ('observado', 'Observado'),
    )
    resultado_dictamen = models.CharField(max_length=200,null=True, blank=True, choices=DICTAMEN_OPCIONES)
    observacion = models.CharField(max_length=2000,null=True, blank=True)
    dictamen_mov = models.OneToOneField(Movimiento, on_delete=models.CASCADE,null=True, blank=True,related_name='dictamen_mov')
    informe = models.FileField(null=True, blank=True)

#importaciones:
#from apps.trabajoFinalApp.models import Proyecto,Cstf,Miembro_Cstf,Tribunal,Miembro_Titular,Miembro_Suplente,RegistroDirector,Integrante,Movimiento,ArchivosTF,Dictamen

##Consuta de un PTF para saber su estado
#proyecto= Proyecto.objects.get(id=1)
#estado = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__movimiento_proyecto__id=proyecto.id).order_by('dictamen_mov__fecha_mov').latest('dictamen_mov_id')
#print('Movimiento y estado: '+estado.dictamen_mov.get_tipo_mov_display(),estado.get_resultado_dictamen_display()) 


##Listado de los PTF según su estado, por rangos de fecha.
#proyectos = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto').filter(dictamen_mov__fecha_mov__range=['2020-01-01', '2027-12-31']).order_by('resultado_dictamen')
#print(proyectos)

##Listado de Tribunales Evaluadores y PTF que tienen asignados, por estados y por rangos de fecha.
#ptfs_asignados = Dictamen.objects.select_related('dictamen_mov__movimiento_proyecto__tribunal_proyecto').filter(resultado_dictamen="aceptado",dictamen_mov__fecha_mov__range=['2020-01-01', '2027-12-31']).values()
#print(ptfs_asignados)































##CONSOLA
#from apps.trabajoFinalApp.models import Proyecto,Cstf,Miembro_Cstf,Tribunal,Miembro_Titular,Miembro_Suplente,RegistroDirector,Integrante,Movimiento,ArchivosTF,Dictamen
#e=Movimiento.objects.select_related('movimiento_proyecto','dictamen_mov').order_by('fecha_mov').filter(movimiento_proyecto__id=proyecto.id).latest('movimiento_proyecto_id')
#print('Movimiento y estado: '+e.get_tipo_mov_display(),e.dictamen_mov.resultado_dictamen)
#listado = Movimiento.objects.select_related('movimiento_proyect','dictamen_mov').order_by('dictamen_mov__resultado_dictamen').filter(fecha_mov__range=['2020-01-01', '2027-12-31'])
#Persona.objects.get(id=1)
#proyecto = Proyecto(titulo='Estudio de malware.',descripcion='Analizar y comprender',presentacion_ptf='2006-10-25')
#integrante = Integrante(alta_proyecto='2021-10-25',baja_proyecto='2024-10-25')
#alumno = Alumno.objects.get(id=4)
#proyecto = Proyecto.objects.get(id=1) 
#miembro_cstf = Miembro_Cstf()
#docente = Docente.objects.get(id=7)
#tribunal = Tribunal(disposicion='2010-10-25',nro_disposicion='333648')
#docente= Docente(nombre='marcos',apellido='gomez',dni='40598544',cuil="20-40598544-3")
#docente= Docente(nombre='marcosZZ',apellido='gomezEE',dni='87654321',cuil="10-40598544-1")
#docente= Docente(nombre='marcosDD',apellido='gomezSS',dni='11114444',cuil="30-40598544-2")
#alumno = Alumno(nombre='marcos',apellido='gomez',dni='40598544',mu="01327",email="m@hotmail.com")
#asesor = Asesor(nombre='Juliano',apellido='Diaz',dni='12345678')
#alumno.save()
#docente = Docente.objects.get(id=5)

#from apps.persona.models import  Docente,Alumno,Asesor
# >>> from apps.trabajoFinalApp.models import  Miembro_Cstf
# >>> from apps.persona.models import Docente
# >>> miembro = Miembro_Cstf()
# >>> docente = Docente.objects.get(id=7)
# >>> from apps.trabajoFinalApp.models import  Miembro_Cstf,Cstf
# >>> cstf = Cstf.objects.get(id=1)       
# >>> miembro.comision_cstf = cstf
# >>> miembro.docente = docente
# >>> miembro.save()
# >>> docente = Docente.objects.get(id=8)
# >>> miembro = Miembro_Cstf()
# >>> miembro.docente = docente
# >>> miembro.comision_cstf = cstf
# >>> miembro.save()
# >>> docente = Docente.objects.get(id=5)
# >>> miembro = Miembro_Cstf()
# >>> miembro.docente = docente
# >>> miembro.comision_cstf = cstf
# >>> miembro.save()
# >>> from apps.trabajoFinalApp.models import  Miembro_Cstf,Cstf,Proyecto
# >>> proyecto = Proyecto.objects.get(id=1)
# >>> tribunal = Tribunal(disposicion='2010-10-25',nro_disposicion='333648')
# >>> from apps.trabajoFinalApp.models import Miembro_Titular
# >>> from apps.trabajoFinalApp.models import  Miembro_Cstf,Cstf,Proyecto,Tribunal,Miembro_Titular,Miembro_Suplente
# >>> from apps.persona.models import  Docente,Alumno,Asesor
# >>> docente = Docente.objects.get(id=8)
# >>> tribunal = Tribunal(disposicion='2010-10-25',nro_disposicion='333648')
# >>> tribunal.presidente = docente
# >>> tribunal.save()
# >>> proyecto = Proyecto.objects.get(id=1) 
# >>> tribunal.proyecto = proyecto
# >>> tribunal.save()
# >>> docente2 = Docente.objects.get(id=7) 
# >>> miembro_titular = Miembro_Titular()
# >>> tribunal_titular = tribunal          
# >>> miembro_titular = Miembro_Titular()
# >>> miembro_titular.tribunal_mt = tribunal
# >>> miembro_titular.vocal_titular = docente 
# >>> miembro_titular.save()                 
# >>> tribunal = Tribunal.objects.get(id=1)   
# >>> miembro_titular.tribunal_mt = tribunal  
# >>> tribunal.save()                        
# >>> miembro_titular.save()
# >>> miembro_titular = Miembro_Titular.objects.get(id=1)  
# >>> tribunal = Tribunal.objects.get(id=1)  
# >>> miembro_titular.tribunal_mt = tribunal  
# >>> tribunal.save()                        
#tribunales = Movimiento.objects.prefetch_related('movimiento_proyect','dictamen_mov','tribunal_proyecto').order_by('dictamen_mov__resultado_dictamen').filter(fecha_mov__range=['2020-01-01', '2027-12-31'])
#tribunales = Proyecto.objects.prefetch_related('tribunal_proyecto_set')
#tribunales = Tribunal.objects.select_related('tribunal_proyecto')
#proyectos = Dominio.objects.all().prefetch_related('movimiento_proyect','dictamen_mov')
#proyecos = Dictamen.objects.all().select_related("dictamen_mov").prefetch_related("dictamen_mov__movimiento_proyect")
#tribunales = Tribunal.objects.select_related('tribunal_proyecto')
#tribunales = Tribunal.objects.select_related('tribunal_proyecto')
#proyectos = Proyecto.objects.all().prefetch_related('movimiento_proyect', 'tribunal_proyecto')
#proyectos = Proyecto.objects.prefetch_related('movimiento')
##Dictamen.objects.prefetch_related(Prefetch('dictamen_mov', queryset=Restaurant.objects.select_related('best_pizza')))
#Dictamen.objects.select_related('dictamen_mov__movimiento_proyect')
#proyectos=Movimiento.objects.prefetch_related('dictamen_mov', queryset=Movimiento.objects.all())