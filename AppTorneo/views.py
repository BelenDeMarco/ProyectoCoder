from django.shortcuts import render
from django.http import HttpResponse
from AppTorneo.models import Equipo, Torneo, Sede, Avatar
from AppTorneo.forms import TorneoFormulario, SedeFormulario, UserRegisterForm, UserEditForm, UserAuthenticationForm, AvatarFormulario

from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView 

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import User


def inicio (request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        #Avatar.objects.filter(user=request.user.id)[0].imagen.url 
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    
    return render(request, 'AppTorneo/inicio.html', diccionario)
       
    #return render(request, 'AppTorneo/inicio.html')
    

def presentacion (request):

    return render(request, 'AppTorneo/presentacion.html')   


def torneos (request):
   
    return render(request, 'AppTorneo/torneos.html')

#Torneos
@login_required
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


def buscar (request):

    if request.GET["sede"]:
        
        sede = request.GET["sede"]
       
        torneos = Torneo.objects.filter(sede__icontains = sede)
    
        return render (request,'AppTorneo/resultadoBusquedaTorneo.html', {"sede": sede, "torneos": torneos})

    else: 

        respuesta = "Problema --> No se ingresaron datos en el buscador"

        return render (request,'AppTorneo/resultadoBusquedaTorneo.html', {"respuesta": respuesta})

#views equipos

class EquipoList(ListView):
    model=Equipo
    template_name="AppTorneo/equipos_list.html"

class EquipoDetalle(DetailView):
    model=Equipo
    template_name="AppTorneo/equipo_detalle.html"


class EquipoCreacion(LoginRequiredMixin, CreateView):

    model=Equipo
    success_url = "../AppTorneo/equipo/list"
    fields= ['nombre','localidad','torneo']


class EquipoUpdate(LoginRequiredMixin, UpdateView):
    model=Equipo
    success_url = "../equipo/list"
    fields= ['nombre','localidad','torneo']


class EquipoDelete(LoginRequiredMixin, DeleteView):
    model=Equipo
    success_url = "../equipo/list"


#views sedes
@login_required
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

@login_required
def eliminarSede (request, sede_id):

    sedeQueQuieroBorrar = Sede.objects.get(id = sede_id)
    sedeQueQuieroBorrar.delete ()

    sedes = Sede.objects.all ()
    return render (request, "AppTorneo/leerSedes.html", {"sedes":sedes})

@login_required
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


def login_request(request):

    if request.method =="POST":
        
        form = UserAuthenticationForm (request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:

                login(request, user)                
                return render(request, "AppTorneo/inicio.html", {"mensaje":f"Sesion iniciada con exito!"})
                
            else:               
                return render(request, "AppTorneo/inicio.html", {"mensaje":f"Los datos ingresados son incorrectos"})
                           
        else:           
            return render(request, "AppTorneo/inicio.html", {"mensaje":f"Error: los datos ingresados son incorrectos"})
               
    form = UserAuthenticationForm()  
    
    return render(request, "AppTorneo/login.html", {"form":form} )


#registro
def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']    
                  form.save()    
                  return render(request,"AppTorneo/inicio.html" ,  {"mensaje":f"USUARIO {username} creado con exito!"})

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

@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) 

            if miFormulario.is_valid():   #Si pasó la validación de Django

                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppTorneo/inicio.html", {"avatar":avatar.imagen.url})

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppTorneo/agregarAvatar.html", {"miFormulario":miFormulario})