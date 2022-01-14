from django.urls import path 

from AppTorneo import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path ('Inicio', views.inicio, name = "Inicio"),

    path ('Presentacion', views.presentacion, name = "Presentacion"),

    path ('Torneos', views.torneos, name = "Torneos"),

    path ('Equipos', views.equipos, name = "Equipos"),

    path ('Sedes', views.sedes, name = "Sedes"),

    path ('torneosFormulario', views.torneosFormulario, name="TorneosFormulario"),
        
    path ('buscar/', views.buscar),

#URL Equipos
    path('equipo/list', views.EquipoList.as_view(), name='EquipoList'),

    path(r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='EquipoDetail'),        
    path(r'^nuevo$', views.EquipoCreacion.as_view(), name='EquipoNew'),
    path(r'^editar/(?P<pk>\d+)$', views.EquipoUpdate.as_view(), name='EquipoEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EquipoDelete.as_view(), name='EquipoDelete'),

#URL Sedes
    path ('sedesFormulario', views.sedesFormulario, name = "SedesFormulario"),

    path ('leerSedes', views.leerSedes, name = "LeerSedes"),

    path ('eliminarSede/<sede_id>/', views.eliminarSede, name = "EliminarSede"),

    path ('editarSede/<sede_id>/', views.modificarSede, name = "EditarSede"), 

 #URL LOGIN, etc 
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),

#Logout
    path('logout', LogoutView.as_view(template_name='AppTorneo/logout.html'), name="Logout"),

#editarUsuario
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
] 
