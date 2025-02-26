from django import forms
from .models import loginUsuario

class loginUsuario(forms.ModelForm):

    class Meta:
        model = loginUsuario
        # fields = ["nombre_usuario", "email", "tipo_usuario", "nombre", "apellidos"]
        fields ='__all__'

