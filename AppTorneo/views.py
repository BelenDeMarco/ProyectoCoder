from django.shortcuts import render


from django.http import HttpResponse


def inicio (request):

    # return HttpResponse ("Esto es una prueba del inicio")

    return render(request, 'AppTorneo/inicio.html')

def categorias (request):

    return render (request,'AppTorneo/categorias.html' )

def equipos (request):

    return render (request,'AppTorneo/equipos.html' )

def jugadores (request):

    return render (request,'AppTorneo/jugadores.html' )

