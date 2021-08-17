from django.db import models

#IMPORTANTEEEEEE
#instalar siempre el psycopg2 para conectar con postgres .. como? = python -m  pip install psycopg2

#en la terminar python manage.py startapp "nombredelnuevoservicio" para crear una nueva app
#comandos utiles para base de datos
#python manage.py makemigrations (para crear el archivo para migrar cambios a postgres)
#python manage.py migrate (para migrar los archivos)

# Create your models here.
class Domicilio(models.Model):
      calle= models.CharField(max_length=255)
      no_calle=models.IntegerField()
      pais= models.CharField(max_length=255)

      def __str__(self):
           return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'


class Persona(models.Model):
    nombre= models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    #se agrega el foreing key en la tabla persona , en este caso para indicar la clave foranea
    #ForeignKey(clase a la que apunta la clave,en caso de que se elimine algo de la clase,se indica que debe ponerse un valor null,
    #se agrega que se deben aceptar valores null con null=True)
    #otra opcion podria ser que cuando se elimina un registro de la tabla de domicilio ,se elemine tambien
    #el registro que afectaba en la tabla de Persona , para eso se ingresa en la clave foranea
    #ingresar= models.ForeignKey(Domicilio,models.CASCADE,null=True) y elimina el registro de la otra tabla
    domicilio=models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)
   #la funcion str se usa para que en el site admin se pueda leer el contenido del objeto
    def __str__(self):
       return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'

