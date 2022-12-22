from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Inscrito

class FormInscrito(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horaInscripcion', 'estado', 'observacion']
        widgets = {
            'fechaInscripcion': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ['horaInscripcion']
        



