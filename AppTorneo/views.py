from django.shortcuts import render


from django.http import HttpResponse

from AppTorneo.models import Equipo, Torneo, Sede
from AppTorneo.forms import TorneoFormulario


def inicio (request):

    # return HttpResponse ("Esto es una prueba del inicio")

    return render(request, 'AppTorneo/inicio.html')

def presentacion (request):

    return render(request, 'AppTorneo/presentacion.html')   

def torneos (request):
   
    return render(request, 'AppTorneo/torneos.html')

def equipos (request):

    return render (request,'AppTorneo/equipos.html' )

def sedes (request):

    return render (request,'AppTorneo/sedes.html' )


def torneosFormulario(request):

    if request.method == "POST":
        
        miFormulario = TorneoFormulario (request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            torneoInsta = Torneo (nombre = informacion["nombre"], tipo = informacion["tipo"], categoria = informacion ["categoria"], sede = informacion ["sede"],inicio = informacion ["inicio"])

            torneoInsta.save() #guarda en la base de datos

            return render (request,'AppTorneo/torneos.html' )

    else:

        miFormulario = TorneoFormulario ()

    return render (request,'AppTorneo/torneosFormulario.html', {"miFormulario":miFormulario} )  

#busqueda
def buscar (request):

    if request.GET["sede"]:
        
        sede = request.GET["sede"]
       
        torneos = Torneo.objects.filter(sede__icontains = sede)
    
        return render (request,'AppTorneo/resultadoBusquedaTorneo.html', {"sede": sede, "torneos": torneos})

    else: 

        respuesta = "Problema --> No se ingresaron datos en el buscador"

        return render (request,'AppTorneo/resultadoBusquedaTorneo.html', {"respuesta": respuesta})

