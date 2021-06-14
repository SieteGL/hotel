from django.db import models
#
from django.utils import timezone
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    #TIPO-EMPLEADO
    ADMINISTRADOR = '0'
    EMPLEADO = '1'
    CLIENTE = '2'
    #GENEROS
    HOMBRE = 'H'
    MUJER = 'M'
    OTRO  = 'O'
    #
    USER_CHOICES = [
        (ADMINISTRADOR,'Administrador'),
        (EMPLEADO,'Empleado'),
        (CLIENTE,'Cliente'),        
    ]

    GENDER_CHOICES = [
        (HOMBRE,'Hombre'),
        (MUJER,'Mujer'),
        (OTRO,'Otro'),
    ]

    tipo_usuario = models.CharField(
        'Tipo usuario',
        max_length=1,
        choices=USER_CHOICES,
        blank=True
    )

    run = models.CharField(
        'Rol Único Nacional',
        max_length=13,
        blank=True
    )

    nombre = models.CharField(
        'Nombre del usuario',
        max_length=20,
        blank=True
    )

    apellido_paterno = models.CharField(
        'Apellido paterno del usuario',
        max_length=20,
        blank=True
    )


    apellido_materno = models.CharField(
        'Apellido materno del usuario',
        max_length=20,
        blank=True
    )

    sexo = models.CharField(
        'Sexo usuario',
        choices=GENDER_CHOICES,
        max_length=1,
        null=True
                
    )    

    fecha_nacimiento = models.DateField(
        'Fecha nacimiento usuario',
        null=True        
    )

    contacto = models.PositiveIntegerField(
        'Número de contacto',
        blank=True,
        null=True
    )

    email = models.EmailField(
        'Email del usuario',
        unique=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    #
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['nombre']

    #manager objects
    objects = UserManager()


    class Meta:
        verbose_name = "Usuario registrado"
        verbose_name_plural = "Usuarios registrados"

    def __str__(self):
        return str(self.nombre)+' - '+str(self.tipo_usuario) 
