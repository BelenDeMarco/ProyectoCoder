from django.db import models

# Create your models here.
class Torneo (models.Model):

    tipo= models.CharField(max_length=40)

    categoria = models.CharField(max_length=40)

    sede = models.CharField(max_length=40)

    horario = models.CharField(max_length=40)

    inicio = models.DateField()

    inscripcion = models.CharField(max_length=40)

class Sede (models.Model):

    nombre = models.CharField(max_length=40)

    ubicacion = models.CharField(max_length=40)

    estacionamiento = models.CharField(max_length=40)

    vestuarios = models.CharField(max_length=40)

class Equipo (models.Model):

    nombre = models.CharField(max_length=40)

    puntos = models.IntegerField()
    

class Jugador (models.Model):

    nombre = models.CharField(max_length=40)

    apellido = models.CharField(max_length=40)

    habilitado = models.BooleanField ()

    