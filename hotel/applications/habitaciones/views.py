from django.shortcuts import render

from django.views.generic import(
    ListView,
)
#from .managers import HabitacionesManagers

from .models import Habitaciones

#view se comunica con el html recive toda su data
class HabitacionesList(ListView):
    template_name = 'habitacion/lista.html'
    context_object_name = 'habitacion'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Habitaciones.objects.buscar_habitaciones(kword, order)        
        return queryset


class MODEL_NAMECreateView(CreateView):
    model = MODEL_NAME
    template_name = "TEMPLATE_NAME"


class MODEL_NAMEUpdateView(UpdateView):
    model = MODEL_NAME
    template_name = "TEMPLATE_NAME"
    
        

        