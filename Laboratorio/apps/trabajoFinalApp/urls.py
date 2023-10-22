from django.urls import path

from apps.trabajoFinalApp import views
# from .views import proyecto_lista


app_name = 'proyecto'
urlpatterns = [
    path('', views.proyecto_lista, name='proyecto_lista'),
]