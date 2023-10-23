from django.urls import path

from apps.trabajoFinalApp import views
# from .views import proyecto_lista


app_name = 'proyecto'
urlpatterns = [
    path('estadisticas/', views.proyecto_lista, name='proyecto_lista'),
    path('crear/', views.proyecto_create, name='proyecto_create'),
    path('registro/', views.proyecto_registro, name='proyecto_registro'),
]