from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'input-group-field',
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'input-group-field',
            }
        )
    )

    class Meta:
        #Meta definition for Userform

        model = User
        fields = (
            'email',            
            'run',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'sexo',
            'fecha_nacimiento',
            'contacto',
            
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),            
            'run': forms.TextInput(
                attrs={
                    'placeholder': 'run ...',
                    'class': 'input-group-field',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre ...',
                    'class': 'input-group-field',
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido paterno ...',
                    'class': 'input-group-field',
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido materno ...',
                    'class': 'input-group-field',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'placeholder': 'sexo ...',
                    'class': 'input-group-field',
                }
            ),
            'contacto': forms.TextInput(
                attrs={
                    'placeholder': 'contacto  ...',
                    'class': 'input-group-field',
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    #usa objects de django para envio de data forms.charfield
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-group-field',
                'placeholder': 'contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):

    class Meta:
        #vista usuario avanzado
        model = User
        fields = (
            'email',
            'tipo_usuario', 
            'run',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'sexo',
            'fecha_nacimiento',
            'contacto',
            'is_active'
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico ...',
                    'class': 'input-group-field',
                }
            ),
            'run': forms.TextInput(
                attrs={
                    'placeholder': 'run ...',
                    'class': 'input-group-field',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre ...',
                    'class': 'input-group-field',
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido paterno ...',
                    'class': 'input-group-field',
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'placeholder': 'Apellido materno ...',
                    'class': 'input-group-field',
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'placeholder': 'sexo ...',
                    'class': 'input-group-field',
                }
            ),
            'contacto': forms.TextInput(
                attrs={
                    'placeholder': 'contacto  ...',
                    'class': 'input-group-field',
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),
        }


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )
    