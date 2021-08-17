from django.http import HttpResponse
from django.shortcuts import render

#EN TEMPLATES SE GUARDA EL ARCHIVO HTML!!!!!!!!!!!!!!!!!!


# Create your views here.

#importamos el modelo de persona para obtener datos desde la base de datos
from personas.models import Persona, Domicilio

#Como comentario , un ejempplo de como pasar variables con el archivo html
"""def bienvenido(request):
    #creamos un diccionario para probar como pasar argumentos que se impriman con html
    mensaje={ 'msg1':'se imprime el mensaje 1','msg2':'Se imprime el valor del mensaje 2 '}
    pasamos como segundo argumento el diccionario , tambien se podria pasar directamente
    los valores contenidos dentro del diccionario
    return render(request,'bienvenido.html',mensaje)"""

#usando .objects , se permite realizar acciones sobre la base de datos

def bienvenido(request):
    #se obtiene la cantidad de registros 
    no_personas=Persona.objects.count()
    #se obtiene todos los datos de la tabla o modelo persona
   # personas=Persona.objects.all()
    #agregamos una funcion para que los registros se ordenen por id
    #podemos agregar mas criterios de ordenamiento si separamos por comas
    #por defecto la funciona ordena ascendentemente, y si se quiere orden descendente se pone un sigo menos (-)
    personas= Persona.objects.order_by('id')
    no_domicilios=Domicilio.objects.count()
   # domicilios=Domicilio.objects.all()
    domicilios=Domicilio.objects.order_by('id')
    #se envia la variable como si fuera una variable dentro de un diccionario
    #importante que todas las variables vayan dentro de la misma llave, si no , NO FUNCIONA!!!
    return render(request,'bienvenido.html',{'no_personas':no_personas , 'personas':personas,'no_domicilios':no_domicilios,
                 'domicilios':domicilios})

#comentamos las porciones de codigos utilizadas como ejemplo anteriormente
""""
def despedida(request):
    return HttpResponse('Bye Bye desde django')

def contactos(request):
     nombre="Pablo"
     return HttpResponse('Los datos del contacto son:',nombre)
 """

