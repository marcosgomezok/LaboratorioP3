from django.urls import path

from apps.trabajoFinalApp import views
# from .views import proyecto_lista


app_name = 'gestion'
urlpatterns = [
    path('alumno', views.alumno, name='alumno'),
    path('cstf', views.cstf, name='cstf'),
    path('cstf/evaluacion', views.cstf_evaluacion, name='cstf_evaluacion'),
    path('tribunal', views.tribunal, name='tribunal'),
    path('administrador', views.administrador, name='administrador'),
    path('administrador/estadisticas', views.administrador_estadisticas, name='administrador_estadisticas'),
    path('administrador/estadisticas/listado/proyectos', views.proyecto_lista, name='proyecto_lista'),
    path('alumno/proyecto/nuevo', views.proyecto_create, name='proyecto_create'),
    path('registro/', views.proyecto_registro, name='proyecto_registro'),
    path('administrador/cstf/nuevo', views.registro_cstf, name='registro_cstf'),
]