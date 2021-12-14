from django.shortcuts import render


from django.http import HttpResponse


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

