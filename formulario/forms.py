from django import forms
from .models import Relatorio

class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = [
            'nome',
            'data',
            'horarioEntrada',
            'horarioSaida',
            'relatorio',
        ]
        labels = {
            'nome' : 'Nome',
            'data' : 'Data',
            'horarioEntrada': 'Horario de Entrada',
            'horarioSaida': 'Horario de Saida',
            'relatorio': 'Ocorrencias',
        }
        widgets={
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={
                'type':'date',
                'class':'form-control',
                'id': 'calendar',
                'autocomplete': 'off',
            }),
            'horarioEntrada': forms.TimeInput(attrs={
                'type': 'time',
                'class':'form-control',
                'id':'horario',
                'autocomplete': 'off'
            }),
            'horarioSaida': forms.TimeInput(attrs={
                'type':'time',
                'class':'form-control',
                'id':'horario',
                'autocomplete': 'off'
            }),
            'relatorio': forms.Textarea(attrs={'class':'form-control'})
        }