from django.contrib import admin

# Register your models here.
from apps.persona.models import Docente,Alumno,Asesor,Persona


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
