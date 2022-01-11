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

#views equipos
from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView 


class EquipoList(ListView):
    model=Equipo
    template_name="AppTorneo/equipos_list.html"

class EquipoDetalle(DetailView):
    model=Equipo
    template_name="AppTorneo/equipo_detalle.html"

class EquipoCreacion(CreateView):

    model=Equipo
    success_url = "../AppTorneo/equipo/list"
    fields= ['nombre','localidad','torneo']


class EquipoUpdate(UpdateView):
    model=Equipo
    success_url = "../equipo/list"
    fields= ['nombre','localidad','torneo']


class EquipoDelete(DeleteView):
    model=Equipo
    success_url = "../equipo/list"

#views sedes
class SedeList(ListView):
    model=Sede
    template_name="AppTorneo/sedes_list.html"

class SedeDetalle(DetailView):
    model=Sede
    template_name="AppTorneo/sede_detalle.html"

class SedeCreacion(CreateView):

    model=Sede
    success_url = "../AppTorneo/sede/list"
    fields= ['nombre','ubicacion','estacionamiento','vestuarios']


class SedeUpdate(UpdateView):
    model=Sede
    success_url = "../sede/list"
    fields= ['nombre','ubicacion','estacionamiento','vestuarios']


class SedeDelete(DeleteView):
    model=Sede
    success_url = "../sede/list"
