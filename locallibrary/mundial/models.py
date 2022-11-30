from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    bandera = models.URLField(max_length= 200, null= True, blank= True)

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    imagen = models.URLField(blank=True)
    posicion = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    

