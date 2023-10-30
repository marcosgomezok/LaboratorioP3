from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from apps.persona.models import Docente,Alumno,Asesor,Persona
from django.contrib.auth.models import User

def index(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    try:
        if(Alumno.objects.select_related('user').filter(user_id=request.user.id)):
            return HttpResponseRedirect(reverse('gestion:alumno'))
        if(Docente.objects.select_related('user').filter(user_id=request.user.id)):
            if(request.user.groups.filter(name='Tribunal')):
                return HttpResponseRedirect(reverse('gestion:tribunal'))
            if(request.user.groups.filter(name='CSTF')):
                return HttpResponseRedirect(reverse('gestion:cstf'))
            else:
                return HttpResponseRedirect(reverse('gestion:docente'))
        if(Asesor.objects.select_related('user').filter(user_id=request.user.id)):
            return HttpResponseRedirect(reverse('gestion:docente'))
        if(request.user.is_superuser):
            return HttpResponseRedirect(reverse('gestion:administrador'))
        
        return HttpResponseRedirect(reverse("usuarios:login"))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("usuarios:login"))


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("usuarios:index"))
        else:
            return render(request, "usuarios/login.html", { "msj": "Credenciales incorrectas" })
    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", { "msj": "Deslogueado" })