from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Anime, LISTA_GENEROS, DIAS_SEMANA, LISTA_TIPO, Usuario
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required
# ...
class Calendario(View):
    template_name = "calendario.html"

    def get(self, request, *args, **kwargs):
        # Obtém a lista de animes para cada dia da semana
        animes_por_dia = {dia[0]: Anime.objects.filter(dia_semana=dia[0]) for dia in DIAS_SEMANA}
        
        # Obtém o dia selecionado (se houver)
        dia_selecionado = request.GET.get('dia', None)
        
        # Obtém os animes correspondentes ao dia selecionado
        animes_selecionados = animes_por_dia.get(dia_selecionado, []) if dia_selecionado else []

        context = {
            'animes_por_dia': animes_por_dia,
            'dia_selecionado': dia_selecionado,
            'animes_selecionados': animes_selecionados,
        }

        return render(request, self.template_name, context)


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

# Em sua view ListaAnimes
class ListaAnimes(ListView):
    template_name = "animes.html"
    model = Anime

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generos'] = LISTA_GENEROS
        context['tipos'] = LISTA_TIPO
        context['anos'] = Anime.objects.dates('data_criacao', 'year', order='DESC')

        # Adicione as seguintes linhas para garantir que os valores de filtro sejam mantidos
        context['genero_filtrado'] = self.request.GET.get('genero', '')
        context['tipo_filtrado'] = self.request.GET.get('tipo', '')
        context['ano_filtrado'] = self.request.GET.get('ano', '')

        return context

    def get_queryset(self):
        genero = self.request.GET.get('genero')
        tipo = self.request.GET.get('tipo')
        ano = self.request.GET.get('ano')

        queryset = Anime.objects.all()

        if genero:
            queryset = queryset.filter(generos__generos=genero)

        if tipo:
            queryset = queryset.filter(tipo=tipo)

        if ano:
            queryset = queryset.filter(data_criacao__year=ano)

        return queryset




class ListaEpisodios(ListView):
    template_name = "episodios.html"
    model = Anime
    #object_view é a lista de itens do modelo


# class Temporada(ListView):
#     template_name = "temporada.html"
#     model = Anime
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
        
class Cadastrar(FormView):
    template_name = "cadastrar.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('anime:login')
    
class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email'] # na tabela usuário mostra esses campos
    
    def get_success_url(self):
        return reverse('anime:homepage')
    
@login_required
def lista_animes_vistos(request):
    animes_vistos = request.user.animes_vistos.all()
    return render(request, 'lista_animes_vistos.html', {'animes_vistos': animes_vistos})

def marcar_visto(request):
    if request.method == 'POST':
        anime_id = request.POST.get('anime_id')
        anime = get_object_or_404(Anime, id=anime_id)
        if anime in request.user.animes_vistos.all():
            request.user.animes_vistos.remove(anime)
        else:
            request.user.animes_vistos.add(anime)
    return redirect('anime:detalhesAnime', pk=anime_id)

def desmarcar(request, pk):
    if request.method == 'POST':
        anime = get_object_or_404(Anime, id=pk)
        # Verifica se o anime está na lista de assistidos antes de remover
        if anime in request.user.animes_vistos.all():
            request.user.animes_vistos.remove(anime)
    return redirect('anime:detalhesAnime', pk=pk)


class Visualizados(ListView):
    template_name = "visualizados.html"
    model = Anime