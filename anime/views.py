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
    template_name = "index.html"
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