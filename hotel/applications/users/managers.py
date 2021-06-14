from django.db import models
#
from django.contrib.auth.models import BaseUserManager
#
from django.utils import timezone

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, tipo_usuario,is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            tipo_usuario=tipo_usuario,            
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    #Crear valores por defecto para el SUPERUSER
    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 0 ,True, True, True, **extra_fields)    

    #Crear valores por defecto para el empleado
    def create_employee(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 1 ,True, False, True, **extra_fields)

    #Crear valores por defecto para el Cliente
    def create_client(self, email, password=None, **extra_fields):
        return self._create_user(email, password, 2 ,False, False, True, **extra_fields)

    #sistemalog
    def usuarios_sistema(self):
        return self.filter(
            is_superuser=False
        ).order_by('-last_login')