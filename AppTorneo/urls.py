from django.urls import path 

from AppTorneo import views


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
    path('sede/list', views.SedeList.as_view(), name='SedeList'),

    path(r'^(?P<pk>\d+)$', views.SedeDetalle.as_view(), name='SedeDetail'),       
    path(r'^nuevo$', views.SedeCreacion.as_view(), name='SedeNew'),
    path(r'^editar/(?P<pk>\d+)$', views.SedeUpdate.as_view(), name='SedeEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.SedeDelete.as_view(), name='SedeDelete'),
    
] 