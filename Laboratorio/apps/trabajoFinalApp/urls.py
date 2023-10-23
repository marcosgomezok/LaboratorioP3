from django.urls import path

from apps.trabajoFinalApp import views
# from .views import proyecto_lista


app_name = 'proyecto'
urlpatterns = [
    path('estadisticas/', views.proyecto_lista, name='proyecto_lista'),
    path('create/', views.proyecto_create, name='proyecto_create'),
]