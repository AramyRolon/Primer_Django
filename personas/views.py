from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

#agregamos la funcion
from personas.PersonaForm import PersonaForm, DomicilioForm
from personas.models import Persona, Domicilio


def detallePersona(request,id):
     #para obtener como busqueda la informacion de la persona usando el id recibido como parametro
     #persona=Persona.objects.get(pk=id)
     #agregamos una funcion mas conveniente para que cuando ocurra un error , nos tire un error 404
     persona= get_object_or_404(Persona,pk=id)
     return render(request,'persona/detalles.html',{'persona':persona})

#e crea una nueva clase del tipo formulario
#como se genera un error, se agrega la opcion de excluir, como no se excluyen ningunos de los campos se indica asi []
#PersonaForm= modelform_factory(Persona,exclude=[]) comentamos para crear una clase tipo forms para personalizar los datos

def NuevaPersona(request):
     #creamos in condicional para que se envien los datos  a la base de datos
     #cuando el metodo del form es "get", se muestran los datos en el url y no es deseable
     #por eso es conveniente poner el metodo "post"
     if request.method =='POST':
          #obtiene los datos ingresados
          formPersona= PersonaForm(request.POST)
          if formPersona.is_valid(): #si los datos ingresados son validos , se guarda en la base de datos
                 formPersona.save()
               #agregamos la funcion de que cuando se carguen los datos , nos redireccione a la pagina de inicio
                 return redirect('inicio')
     else: #si no se obtiene los datos se espera
          #instanciando la clase de tipo formulario,creamos un objeto
          formPersona=PersonaForm()
     #todos los casos llevan a que se tiene que volver a visualizar la pagina
     return render(request,'persona/nuevo.html',{'formPersona':formPersona})

def EditarPersona(request,id): #casi el mismo caso que con crear una nueva persona
     persona= get_object_or_404(Persona,pk=id)
     if request.method =='POST':
          #para que reconozca que se edita un dato y no que no sea tomado como un nuevo dato
          formPersona= PersonaForm(request.POST,instance=persona)
          if formPersona.is_valid(): #si los datos ingresados son validos , se guarda en la base de datos
                 formPersona.save() #como se obtiene la instancia de un modelo, Django realiza la funcion save como update en la base de datos
                 return redirect('inicio')
     else:
          formPersona=PersonaForm(instance=persona)
     #todos los casos llevan a que se tiene que volver a visualizar la pagina
     return render(request,'persona/editar.html',{'formPersona':formPersona})

def EliminarPersona(request,id): #casi el mismo caso que con crear una nueva persona
     persona= get_object_or_404(Persona,pk=id) #se obtiene el objeto por medio del id
     if persona: #si encuentra el objeto , lo elimina
        persona.delete()
        return redirect('inicio') #luego lo redirecciona a la pagina de inicio


def DetalleDomicilio(request, id):
         domicilio= get_object_or_404(Domicilio, pk=id)
         return render(request, 'domicilio/detalles.html', {'domicilio': domicilio})


def NuevoDomicilio(request):
    if request.method == 'POST':
        formDomicilio = DomicilioForm(request.POST)
        if formDomicilio.is_valid():  # si los datos ingresados son validos , se guarda en la base de datos
            formDomicilio.save()
            # agregamos la funcion de que cuando se carguen los datos , nos redireccione a la pagina de inicio
            return redirect('inicio')
    else:  # si no se obtiene los datos se espera
        # instanciando la clase de tipo formulario,creamos un objeto
        formDomicilio = DomicilioForm()
    # todos los casos llevan a que se tiene que volver a visualizar la pagina
    return render(request, 'domicilio/nuevo.html', {'formDomicilio': formDomicilio})


def EditarDomicilio(request, id):  # casi el mismo caso que con crear una nueva persona
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        # para que reconozca que se edita un dato y no que no sea tomado como un nuevo dato
        formDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formDomicilio.is_valid():  # si los datos ingresados son validos , se guarda en la base de datos
            formDomicilio.save()  # como se obtiene la instancia de un modelo, Django realiza la funcion save como update en la base de datos
            return redirect('inicio')
    else:
        formDomicilio = DomicilioForm(instance=domicilio)
    # todos los casos llevan a que se tiene que volver a visualizar la pagina
    return render(request, 'domicilio/editar.html', {'formDomicilio': formDomicilio})


def EliminarDomicilio(request, id):  # casi el mismo caso que con crear una nueva persona
    domicilio = get_object_or_404(Domicilio, pk=id)  # se obtiene el objeto por medio del id
    if domicilio:  # si encuentra el objeto , lo elimina
        domicilio.delete()
        return redirect('inicio')  # luego lo redirecciona a la pagina de inicio


