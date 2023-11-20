from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Anime
from django.views.generic import TemplateView, ListView, DetailView
# Create your views here.


#def homepage(request):
#    context = {}
#    lista_animes = Anime.objects.all()
#    context['lista_animes'] = lista_animes
#    return render(request, "index.html",context)

class Homepage(ListView):
    template_name = "homepage.html"
    model = Anime
    #object_view é a lista de itens do modelo

class ListaAnimes(ListView):
    template_name = "animes.html"
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