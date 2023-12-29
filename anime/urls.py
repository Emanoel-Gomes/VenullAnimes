# urls.py
from django.urls import path, reverse_lazy
from .views import (
    Homepage,
    DetalhesAnime,
    ListaAnimes,
    PesquisaAnime,
    EditarPerfil,
    Cadastrar,
    ListaEpisodios,
    Calendario,
    Temporada,
    ListaGeneros,
    ListaPorGenero,
    marcar_visto,
    Visualizados,
    desmarcar,
)
from django.contrib.auth import views as auth_views

app_name = 'anime'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('animes/', ListaAnimes.as_view(), name='animes'),
    path('episodios/', ListaEpisodios.as_view(), name='episodios'),
    path('calendario/', Calendario.as_view(), name='calendario'),
    path('lista_generos/', ListaGeneros.as_view(), name='lista_generos'),
    path('lista_por_genero/<str:genero>/', ListaPorGenero.as_view(), name='lista_por_genero'),
    path('temporada/', Temporada.as_view(), name='temporada'),
    path('animes/<int:pk>', DetalhesAnime.as_view(), name='detalhesAnime'),
    path('pesquisa/', PesquisaAnime.as_view(), name='pesquisaAnime'),
    path('perfil/<int:pk>', EditarPerfil.as_view(), name='editarperfil'),
    path('cadastrar/', Cadastrar.as_view(), name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('mudarsenha/', auth_views.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('anime:homepage')), name='mudarsenha'),
    path('marcar_visto/', marcar_visto, name='marcar_visto'),
    path('visualizados/', Visualizados.as_view(), name='visualizados'),
    path('desmarcar/<int:pk>/', desmarcar, name='desmarcar_anime'),


    

]
