from django.urls import path 

from AppTorneo import views


urlpatterns = [

    path ('Inicio', views.inicio, name = "Inicio"),

    path ('Categorias', views.categorias, name = "Categorias"),

    path ('Equipos', views.equipos, name = "Equipos"),

    path ('Jugadores', views.jugadores, name = "Jugadores"),
    
] 