from django.contrib import admin

# Register your models here.
from apps.persona.models import Docente,Alumno,Asesor,Persona
from apps.trabajoFinalApp.models import Proyecto,Cstf,Miembro_Cstf,Tribunal,Miembro_Titular,Miembro_Suplente,RegistroDirector,Integrante,Movimiento,ArchivosTF,Dictamen


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido")

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","cuil")

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","dni","mu")

@admin.register(Asesor)
class AsesorAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","cuil")

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("id","titulo")

@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display = ("id","proyecto_id")

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ("id","tipo_mov")
@admin.register(Dictamen)
class DictamenAdmin(admin.ModelAdmin):
    list_display = ("id","resultado_dictamen")
@admin.register(Cstf)
class CstfAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_creacion")
@admin.register(RegistroDirector)
class RegistroDirectorAdmin(admin.ModelAdmin):
    list_display = ("id","alta_proyecto")
@admin.register(Tribunal)
class TribunalAdmin(admin.ModelAdmin):
    list_display = ("id","disposicion")
@admin.register(Miembro_Suplente)
class Miembro_SuplenteAdmin(admin.ModelAdmin):
    list_display = ("id","vocal_suplente_id")
