from django.db import models

# Create your models here.
class Categoria (models.Model):

    nombre= models.CharField(max_length=40)

    tipo = models.CharField(max_length=40)

    inscripcion = models.BooleanField ()


class Equipo (models.Model):

    nombre = models.CharField(max_length=40)

    puntos = models.IntegerField()
    

class Jugador (models.Model):

    nombre = models.CharField(max_length=40)

    apellido = models.CharField(max_length=40)

    habilitado = models.BooleanField ()

    