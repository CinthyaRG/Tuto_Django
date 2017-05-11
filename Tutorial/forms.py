from django import forms
from Tutorial.models import Usuarios


class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ['first_name','last_name','email']

        labels = {
            'first_name': 'Nombre: ',
            'last_name': 'Apellido: ',
            'email': 'Correo: '
        }