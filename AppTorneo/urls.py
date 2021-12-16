from django.urls import path 

from AppTorneo import views


urlpatterns = [

    path ('Inicio', views.inicio, name = "Inicio"),

    path ('Presentacion', views.presentacion, name = "Presentacion"),

    path ('Torneos', views.torneos, name = "Torneos"),

    path ('Equipos', views.equipos, name = "Equipos"),

    path ('Jugadores', views.jugadores, name = "Jugadores"),

    path ('torneoFormulario', views.torneoFormulario, name="torneoFormulario"),
    
] 