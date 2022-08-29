from django import forms
from .models import Bodega, Delegacion, Universidad, Bodeguero, Elemento, Ciudad, Region, Deportista, Tiene


class BodegueroForm(forms.ModelForm):
    class Meta:
        model = Bodeguero
        fields = ['nombre']

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ["nombre", "direccion", "descripcion", "estado", "bodeguero"]
