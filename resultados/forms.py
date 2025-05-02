from django import forms
from .models import Resultado

class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Resultado
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }