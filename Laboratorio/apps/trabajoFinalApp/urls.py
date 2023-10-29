from django.urls import path

from apps.trabajoFinalApp import views

app_name = 'gestion'
urlpatterns = [
    path('alumno/', views.alumno, name='alumno'),
    path('docente/', views.docente, name='docente'),
    path('cstf', views.cstf, name='cstf'),
    path('cstf/evaluacion', views.cstf_evaluacion, name='cstf_evaluacion'),
    path('tribunal', views.tribunal, name='tribunal'),
    path('tribunal/evaluacion/ptf', views.tribunal_evaluacion_ptf, name='tribunal_evaluacion_ptf'),
    path('tribunal/evaluacion/borrador', views.tribunal_evaluacion_borrador, name='tribunal_evaluacion_borrador'),
    path('administrador', views.administrador, name='administrador'),
    path('administrador/estadisticas', views.administrador_estadisticas, name='administrador_estadisticas'),
    path('administrador/estadisticas/listado/proyectos', views.proyecto_lista, name='proyecto_lista'),
    path('administrador/alumno/alta', views.administrador_alumno_alta, name='administrador_alumno_alta'),
    path('administrador/docente/alta', views.administrador_docente_alta, name='administrador_docente_alta'),
    path('administrador/asesor/alta', views.administrador_asesor_alta, name='administrador_asesor_alta'),
    path('alumno/proyecto/estado', views.proyecto_create, name='proyecto_create'),
    path('alumno/proyecto/integrante', views.proyecto_integrante, name='proyecto_integrante'),
    path('alumno/proyecto/baja', views.proyecto_baja, name='proyecto_baja'),
    path('alumno/proyecto/entrega', views.proyecto_entrega, name='proyecto_entrega'),
    path('registro/', views.proyecto_registro, name='proyecto_registro'),
    path('administrador/cstf/nuevo', views.registro_cstf, name='registro_cstf'),
    path('administrador/tribunal/nuevo', views.tribunal_nuevo, name='tribunal_nuevo'),
]