#se declara la clase de PersonaForm para tener de manera personalizada cada objeto del formulario
from django.forms import ModelForm, EmailInput, TextInput

#indicamos que recibe dat tipo modelo de form , modelos de formulario , donde el model son los que
#se usan en la base de datos , modelos de base de datos
from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    #class meta se usa para ordenar y controlar los registros cuando se devuelven datos en una consulta
    class Meta:
         model=Persona #el modelo utilizado
         fields= '__all__' #se indica que se usan todos los campos
         widgets= {
               'email':EmailInput(attrs={'type':'email'})
         }

class DomicilioForm(ModelForm):
     class Meta:
         model= Domicilio
         fields= '__all__'
         widgets={
              'no_calle': TextInput(attrs={'type':'number'}) #para verificar que se un numero el que se ingrese
         }
