from django.contrib import admin

from django.urls import path,include
from django.views.generic import TemplateView
from django.shortcuts import redirect

urlpatterns = [
     path('core/', include('apps.core.urls')),
     path('admin/', admin.site.urls),
     path('gestion/', include('apps.trabajoFinalApp.urls')),
     path('usuarios/', include('apps.usuario.urls'), name='usuarios'),
     path('', lambda req: redirect('usuarios/login', permanent=False)),
     # path('', TemplateView.as_view(template_name='base/home.html'), name='home'),
]



