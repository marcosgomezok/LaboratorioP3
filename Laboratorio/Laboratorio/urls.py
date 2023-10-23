from django.contrib import admin

from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
     path('core/', include('apps.core.urls')),
     path('admin/', admin.site.urls),
     path('proyecto/', include('apps.trabajoFinalApp.urls')),
     path('', TemplateView.as_view(template_name='base/home.html'), name='home'),
]



