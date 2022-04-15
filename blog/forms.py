from django import forms
from .models import Perfil

class formulario(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['user','apellido', 'email', 'imagen'] 
        