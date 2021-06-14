from django.db import models

from .managers import HabitacionesManagers

# Create your models here.

class Habitaciones(models.Model):
    #TIPO DE CAMAS DISPONIBLES POR HABITACION
    SINGLE = '0'
    DOUBLE = '1'
    KING = '2'
    #TIPOS DE BAÑOS
    SIMPLE = '0'
    MEDIUM = '1'
    AVANZADO = '2'
    #PERSONAS POR HABITACIONES
    UNO = '0'
    DOS = '1'
    TRES = '2'
    
    
    CAMAS_CHOICES = [
        (SINGLE,'Single'),
        (DOUBLE,'Double'),
        (KING,'King'),
    ]

    BAÑOS_CHOICES = [
        (SIMPLE,'Simple'),
        (MEDIUM,'Medium'),
        (AVANZADO,'Avanzado'),
    ]
    CANTIDAD_CHOICES = [
        (UNO,'Uno'),
        (DOS,'Dos'),
        (TRES,'Tres'),
    ]

    numero=models.PositiveIntegerField(
        'numero habitacion',
        blank=True
    )

    tipo_cama = models.CharField(
        'tipo de camas',
        choices=CAMAS_CHOICES,
        max_length=1,
        blank=True
    )
    tipo_baños = models.CharField(
        'tipo de baños',
        choices=BAÑOS_CHOICES,
        max_length=1,
        blank=True
    )
    tipo_cantidad = models.CharField(
        'cantidad de personas por habitacion',
        choices=CANTIDAD_CHOICES,
        max_length=1,
        blank=True
    )

    objects = HabitacionesManagers()

    def get_tipocama(self):
        return ('').join([tipo_cama for tipo_cama in self.tipo_cama[:1]])

    def __str__(self):
        return str(self.id)+' - '+ str(self.numero)+' - '+ str(self.get_tipocama())


    
