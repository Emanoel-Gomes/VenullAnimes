from django import forms
from .models import Usuario,LISTA_GENEROS, LISTA_TIPO
from django.contrib.auth.forms import UserCreationForm


class FiltroAnimeForm(forms.Form):
    genero = forms.ChoiceField(choices=[('', 'Todos')] + list(LISTA_GENEROS))
    tipo = forms.ChoiceField(choices=[('', 'Todos')] + list(LISTA_TIPO))
    ano = forms.IntegerField(min_value=1900, max_value=2100, required=False)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1','password2')