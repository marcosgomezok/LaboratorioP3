from django.urls import path

from apps.trabajoFinalApp import views

app_name = 'gestion'
urlpatterns = [
    path('alumno', views.alumno, name='alumno'),
    path('alumno/proyecto/estado', views.proyecto_create, name='proyecto_create'),
    path('alumno/proyecto/integrante', views.proyecto_integrante, name='proyecto_integrante'),
    path('alumno/proyecto/baja', views.proyecto_baja, name='proyecto_baja'),
    path('alumno/proyecto/entrega', views.proyecto_entrega, name='proyecto_entrega'),
    path('docente', views.docente, name='docente'),
    path('cstf', views.cstf, name='cstf'),
    path('cstf/evaluacion', views.cstf_evaluacion, name='cstf_evaluacion'),
    path('tribunal', views.tribunal, name='tribunal'),
    path('tribunal/evaluacion/ptf', views.tribunal_evaluacion_ptf, name='tribunal_evaluacion_ptf'),
    path('tribunal/evaluacion/borrador', views.tribunal_evaluacion_borrador, name='tribunal_evaluacion_borrador'),
    path('tribunal/evaluacion/final', views.tribunal_evaluacion_final, name='tribunal_evaluacion_final'),
    path('administrador', views.administrador, name='administrador'),
    #path('administrador/estadisticas', views.administrador_estadisticas, name='administrador_estadisticas'),
    #path('administrador/estadisticas/listado/proyectos', views.proyecto_lista, name='proyecto_lista'),
    path('administrador/alumno/alta', views.administrador_alumno_alta, name='administrador_alumno_alta'),
    path('administrador/docente/alta', views.administrador_docente_alta, name='administrador_docente_alta'),
    path('administrador/asesor/alta', views.administrador_asesor_alta, name='administrador_asesor_alta'),
    path('administrador/cstf/nuevo', views.registro_cstf, name='registro_cstf'),
    path('administrador/tribunal/nuevo', views.tribunal_nuevo, name='tribunal_nuevo'),
    path('administrador/proyecto/nuevo', views.administrador_proyecto_alta, name='administrador_proyecto_alta'),
    path('administrador/proyecto/modificar', views.administrador_proyecto_modificar, name='administrador_proyecto_modificar'),
    path('administrador/integrante/alumno', views.administrador_integrante_alumno, name='administrador_integrante_alumno'),
    path('administrador/integrante/director', views.director_cambio, name='director_cambio'),
    path('administrador/movimientos/nuevo', views.movimientos, name='movimientos'),
    path('administrador/movimientos/lista', views.movimiento_lista, name='movimiento_lista'),
    path('administrador/movimientos/lista/detalle', views.movimiento_detalle, name='movimiento_detalle'),
    path('administrador/estadisticas', views.administrador_estadisticas, name='administrador_estadisticas'),
    path('administrador/estadisticas/lista_ptf', views.proyecto_lista, name='proyecto_lista'),
    path('administrador/estadisticas/lista_tribunal', views.tribunal_proyecto_lista, name='tribunal_proyecto_lista'),
]