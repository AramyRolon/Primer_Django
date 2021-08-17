"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personas.views import detallePersona, NuevaPersona, EditarPersona, EliminarPersona, DetalleDomicilio, \
    NuevoDomicilio, EditarDomicilio, EliminarDomicilio
from webapp.views import bienvenido




urlpatterns = [
    path('admin/', admin.site.urls),
    #se le agrega un nombre al url para que sea mas facil sin necesidad de modificar al url
    path('',bienvenido,name='inicio'),
  #  path('despedida/',despedida),
  #  path('contactos.html',contactos)
    #en este path los que se muestra en <> es el tipo de parametro y el nombre del parametro
    path('detalle_persona/<int:id>',detallePersona),
    path('nueva_persona/',NuevaPersona,name='nuevo'),
    path('editar_persona/<int:id>',EditarPersona),
    path('eliminar_persona/<int:id>',EliminarPersona),
    path('ver_domicilio/<int:id>',DetalleDomicilio),
    path('editar_domicilio/<int:id>',EditarDomicilio),
    path('eliminar_domicilio/<int:id>',EliminarDomicilio),
    path('nuevo_domicilio/',NuevoDomicilio,name='nuevo_domicilio')
]
