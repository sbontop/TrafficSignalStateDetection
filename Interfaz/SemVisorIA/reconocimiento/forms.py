from django import forms
from .models import Imagen

class SubirImagenForm(forms.Form):
    imagen = forms.ImageField(required=True,  label='')

    def save(self):
        imagen = self.cleaned_data['imagen']
        imagen_guardar = Imagen(imagen=imagen)
        imagen_guardar.save()
        return imagen_guardar


