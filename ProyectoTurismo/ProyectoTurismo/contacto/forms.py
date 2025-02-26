from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.CharField(label="Email", required=True)

    asunto=forms.CharField(label="Asunto", required=True)

    mensaje=forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)