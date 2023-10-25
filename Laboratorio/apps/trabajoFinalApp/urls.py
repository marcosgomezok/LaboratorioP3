from django.urls import path

from apps.trabajoFinalApp import views
# from .views import proyecto_lista


app_name = 'gestion'
urlpatterns = [
    path('alumno', views.alumno, name='alumno'),
    path('cstf', views.cstf, name='cstf'),
    path('tribunal', views.cstf, name='tribunal'),
    path('administrador', views.cstf, name='administrador'),
    path('estadisticas/', views.proyecto_lista, name='proyecto_lista'),
    path('alumno/proyecto/nuevo', views.proyecto_create, name='proyecto_create'),
    path('registro/', views.proyecto_registro, name='proyecto_registro'),
    path('registro/cstf', views.proyecto_registro_cstf, name='proyecto_registro_cstf'),
]