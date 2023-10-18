from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=8, unique=True)

class Docente(Persona):
    cuil = models.CharField(max_length=200,unique=True)

class Alumno(Persona):
    mu = models.CharField(max_length=200,unique=True)
    email = models.CharField(max_length=200)

class Asesor(Persona):
    cv_asesor = models.FileField(null=True)

