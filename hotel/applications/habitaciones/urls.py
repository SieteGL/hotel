from django.urls import path
from . import views

app_name = "habitaciones_app"

urlpatterns = [
    path(
        'habitaciones/lista/',
        views.HabitacionesList.as_view(),
        name='habitacion-lista'
    )
]