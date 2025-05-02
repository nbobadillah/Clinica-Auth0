from django import forms
from .models import Paciente

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cedula',
            'correo',
            'celular',
            'name',
            
        ]

        labels = {
            'cedula' : 'Cedula',
            'correo' : 'Correo',
            'celular' : 'Celular',
            'name' : 'Name',
            
        }
