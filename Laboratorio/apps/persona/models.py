from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
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

