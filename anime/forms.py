# No seu arquivo forms.py
from django import forms
from .models import LISTA_GENEROS, LISTA_TIPO

class FiltroAnimeForm(forms.Form):
    genero = forms.ChoiceField(choices=[('', 'Todos')] + list(LISTA_GENEROS))
    tipo = forms.ChoiceField(choices=[('', 'Todos')] + list(LISTA_TIPO))
    ano = forms.IntegerField(min_value=1900, max_value=2100, required=False)
