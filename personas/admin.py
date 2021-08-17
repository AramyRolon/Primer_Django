from django.contrib import admin

#PARA CREAR EL SUPERUSUARIO!!!
#comando en la terminal: python manage.py createsuperuser



# Register your models here.
from personas.models import Persona, Domicilio

#se registran las 'clases' o 'tablas' que se crean para la base de datos
#para que estas se muestren cuando ingreso en la pagina del administrador desde el servidor
admin.site.register(Persona)
admin.site.register(Domicilio)
