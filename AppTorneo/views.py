from django.shortcuts import render


from django.http import HttpResponse

from AppTorneo.models import Equipo, Jugador, Torneo
from AppTorneo.forms import JugadorFormulario


def inicio (request):

    # return HttpResponse ("Esto es una prueba del inicio")

    return render(request, 'AppTorneo/inicio.html')

def presentacion (request):

    return render(request, 'AppTorneo/presentacion.html')   

def torneos (request):

    return render (request,'AppTorneo/torneos.html' )

def equipos (request):

    return render (request,'AppTorneo/equipos.html' )

def jugadores (request):

    return render (request,'AppTorneo/jugadores.html' )

def torneosFormulario(request):

    if request.method == "POST":

        torneoInsta = Torneo ( tipo = request.POST['tipo'], categoria = request.POST['categoria'], sede = request.POST['sede'], inicio = request.POST['inicio'])

        torneoInsta.save()

        return render(request, 'AppTorneo/Inicio.html')


    return render(request, 'AppTorneo/torneosFormulario.html')


def equiposFormulario(request):

    if request.method == "POST":

        equipoInsta = Equipo (nombre = request.POST['nombre'], puntos = request.POST ['puntos'])

        equipoInsta.save()

        return render(request, 'AppTorneo/Inicio.html')


    return render(request, 'AppTorneo/equiposFormulario.html')


def jugadoresFormulario(request):

    if request.method == "POST":
        
        miFormulario = JugadorFormulario (request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            jugadorInsta = Jugador (nombre = informacion["nombre"], apellido = informacion["apellido"], habilitado = informacion ["habilitado"])

            jugadorInsta.save() #guarda en la base de datos

            return render (request,'AppTorneo/Inicio.html' )

    else:

        miFormulario = JugadorFormulario ()

    return render (request,'AppTorneo/jugadoresFormulario.html', {"miFormulario":miFormulario} )

#busqueda

def busquedaTorneo (request):

    
    return render(request, 'AppTorneo/busquedaTorneo.html')


def buscar (request):

    if request.GET["sede"]:
        
        sede = request.GET["sede"]
       
        torneos = Torneo.objects.filter(sede__icontains = sede)

        return render (request,'AppTorneo/resultadoBusquedaTorneo.html', {"sede": sede, "torneos": torneos})

    else: 

        respuesta = "No enviaste datos"

    return HttpResponse (respuesta)