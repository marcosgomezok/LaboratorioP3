from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

class Docente(Persona):
    cuil = models.CharField(max_length=200,unique=True,null=True)

class Alumno(Persona):
    dni = models.CharField(max_length=8,null=True)
    mu = models.CharField(max_length=200,unique=True,null=True)
    analitico = models.FileField(null=True)

class Asesor(Persona):
    cuil = models.CharField(max_length=200,unique=True,null=True)
    cv_asesor = models.FileField(null=True)
