from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from apps.persona.models import Docente,Alumno,Asesor

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    #return redirect('gestion/alumno', permanent=False)
    #return render(request, "usuarios/usuario.html")
    try:
        Alumno.objects.select_related('user').get(user_id=request.user.id)
        return HttpResponseRedirect(reverse('gestion:alumno'))
    except Alumno.DoesNotExist:
        return None
    # try:
    #     Alumno.objects.select_related('user').get(user_id=request.user.id)
    #     return HttpResponseRedirect(reverse('gestion:alumno'))
    # except Alumno.DoesNotExist:
    #     return None
    # alumno = Alumno.objects.select_related('user').get(user_id=request.user.id)
    # print(alumno)

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