from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
#
from .models import User

def check_ocupation_user(tipo_usuario, user_tipo_usuario):
    #
    
    if (tipo_usuario == User.ADMINISTRADOR or ocupation == user_tipo_usuario):
        
        return True
    else:
        return False

#acceso a registro como empleado
class RegistroPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_tipo_usuario_user(request.user.tipo_usuario, User.EMPLEADO):
            # NO TIENE AUTORIZACION
            return HttpResponseRedirect(
                reverse(
                    'users_app:user-login'
                )
            )        
        return super().dispatch(request, *args, **kwargs)

#acceso a servicio como empleado
class ServicioPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app:user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        #
        if not check_tipo_usuario_user(request.user.tipo_usuario, User.EMPLEADO):
            # NO TIENE AUTORIZACION
            return HttpResponseRedirect(
                reverse(
                    'users_app:user-login'
                )
            )        
        return super().dispatch(request, *args, **kwargs)

#crear mixing necesarios para los demas modulos
              
