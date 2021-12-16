from django.shortcuts import render


from django.http import HttpResponse

from AppTorneo.models import Equipo, Jugador, Torneo



def torneoFormulario(request):

    if request.method == "POST":

        torneoInsta = Torneo ( request.POST['tipo'], request.POST['categoria'], request.POST['sede'], request.POST['inicio'])

        Torneo.save()

        equipoInsta = Equipo ( request.POST['nombre'])

        Equipo.save()

        jugadorInsta = Jugador ( request.POST['nombre'], request.POST['apellido'])

        Jugador.save()

        return render(request, 'AppTorneo/Inicio')


    return render(request, 'AppTorneo/torneoFormulario.html')

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

