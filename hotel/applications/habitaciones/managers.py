from django.db import models

class HabitacionesManagers(models.Manager):

    def buscar_habitaciones(self, kword, order):
        consulta = self.filter(
            numero__icontains=kword
        )        
        if order == 'numero':
            return consulta.order_by('numero')