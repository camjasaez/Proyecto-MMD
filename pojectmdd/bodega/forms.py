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


class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ["nombre", "descripcion", "tipo"]


class TieneForm(forms.ModelForm):
    class Meta:
        model = Tiene
        fields = ['bodega', 'elemento', 'delegacion']
        widgets = {
            'bodega': forms.Select(attrs={
                'class': "form-select",
                'style': 'max-width: 500px;',
                'placeholder': 'Bodega...'
            }),
            'elemento': forms.Select(attrs={
                'class': "form-select",
                'style': 'max-width: 500px;',
                'placeholder': 'Elemento...'
            }),
            'delegacion': forms.Select(attrs={
                'class': "form-select",
                'style': 'max-width: 500px;',
                'placeholder': 'Delegacion...'
            }),
        }
