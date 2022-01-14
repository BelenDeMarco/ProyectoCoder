from django.shortcuts import render


from django.http import HttpResponse

from AppTorneo.models import Equipo, Torneo, Sede
from AppTorneo.forms import TorneoFormulario, SedeFormulario, UserRegisterForm, UserEditForm


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
def sedesFormulario (request):

    if request.method == "POST":

        miFormulario = SedeFormulario (request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            sedeInsta = Sede(nombre = informacion["nombre"], ubicacion = informacion["ubicacion"], estacionamiento= informacion["estacionamiento"], vestuarios = informacion ["vestuarios"])

            sedeInsta.save() #guarda en la base de datos

            sedes = Sede.objects.all ()
            return render (request, "AppTorneo/leerSedes.html", {"sedes":sedes})

    else:

        miFormulario = SedeFormulario ()

    return render (request,'AppTorneo/sedesFormulario.html', {"miFormulario":miFormulario}) 


def leerSedes (request): 

    sedes = Sede.objects.all() 

    dicc = {"sedes":sedes} #contexto

    return render (request,'AppTorneo/leerSedes.html', dicc)


def eliminarSede (request, sede_id):

    sedeQueQuieroBorrar = Sede.objects.get(id = sede_id)
    sedeQueQuieroBorrar.delete ()

    sedes = Sede.objects.all ()
    return render (request, "AppTorneo/leerSedes.html", {"sedes":sedes})


def modificarSede (request, sede_id):

    sede = Sede.objects.get (id = sede_id)

    if request.method == "POST":

        miFormulario = SedeFormulario (request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            sede.nombre = informacion["nombre"]
            sede.ubicacion = informacion["ubicacion"]
            sede.estacionamiento= informacion["estacionamiento"]
            sede.vestuarios = informacion ["vestuarios"]

            sede.save() #guarda en la base de datos
            sedes = Sede.objects.all ()
            return render (request, "AppTorneo/leerSedes.html", {"sedes":sedes})
           
    else:

        miFormulario = SedeFormulario (initial = {"nombre":sede.nombre, "ubicacion":sede.ubicacion, "estacionamiento":sede.estacionamiento, "vestuarios":sede.vestuarios})

    return render (request,'AppTorneo/editarSede.html', {"miFormulario":miFormulario, "sede_id":sede_id})


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)                
                return render(request, "AppTorneo/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:               
                return render(request, "AppTorneo/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                           
        else:           
            return render(request, "AppTorneo/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
               
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppTorneo/login.html", {"form":form} )


#registro
def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']    
                  form.save()    
                  return render(request,"AppTorneo/inicio.html" ,  {"mensaje":f"USUARIO {username} Creado con exito! Logueate con tu usuario y contraseña"})

      else:
            form = UserRegisterForm()     
            
      return render(request,"AppTorneo/register.html" ,  {"form":form})


@login_required
def editarPerfil(request):
 
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "AppTorneo/inicio.html")
        
    else:       
        miFormulario = UserEditForm(initial={'email':usuario.email})
              
    return render(request, "AppTorneo/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
