from django.contrib import admin

# Register your models here.
from apps.persona.models import Docente,Alumno,Asesor


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","dni","cuil")

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","dni","mu")

@admin.register(Asesor)
class AsesorAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","apellido","dni")
