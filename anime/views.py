from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Anime, Genero, LISTA_GENEROS
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

# ...

class ListaGeneros(View):
    template_name = "lista_generos.html"

    def get(self, request, *args, **kwargs):
        context = {'generos': LISTA_GENEROS}
        return render(request, self.template_name, context)

class ListaPorGenero(View):
    template_name = "lista_por_genero.html"

    def get(self, request, genero, *args, **kwargs):
        animes_por_genero = Anime.objects.filter(generos__generos=genero)
        context = {'animes': animes_por_genero, 'genero': genero}
        return render(request, self.template_name, context)

    
class Homepage(ListView):
    template_name = "homepage.html"
    model = Anime
    #object_view é a lista de itens do modelo

class ListaAnimes(ListView):
    template_name = "animes.html"
    model = Anime
    #object_view é a lista de itens do modelo

class ListaEpisodios(ListView):
    template_name = "episodios.html"
    model = Anime
    #object_view é a lista de itens do modelo
    
class Calendario(ListView):
    template_name = "calendario.html"
    model = Anime
    #object_view é a lista de itens do modelo

class Temporada(ListView):
    template_name = "temporada.html"
    model = Anime
    #object_view é a lista de itens do modelo

class DetalhesAnime(DetailView):
    template_name = "detalhesAnime.html"
    model = Anime
    #object é 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        #selecionar o anime
        anime = self.get_object()
        #contar +1 na visalização
        anime.visualizacoes += 1
        #salvar
        anime.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesAnime, self).get_context_data(**kwargs)
        animes_relacionados = Anime.objects.filter(generos__generos=self.get_object().generos.first()).exclude(pk=self.get_object().pk)
        context["animes_relacionados"] = animes_relacionados
        return context

class PesquisaAnime(ListView):
    template_name = "pesquisa.html"
    model = Anime

    #editando o object_list da classe PesquisaAnime
    def get_queryset(self):
        pesquisa = self.request.GET.get('q')
        if pesquisa:
            object_list = self.model.objects.filter(titulo__contains=pesquisa)
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, TemplateView):
    template_name = "editarPerfil.html"


class Cadastrar(TemplateView):
    template_name = "cadastrar.html"