# url - view - template
from django.urls import path,include
from .views import Homepage,DetalhesAnime,ListaAnimes,PesquisaAnime,EditarPerfil,Cadastrar,ListaEpisodios
from django.contrib.auth import views as auth_view

app_name = 'anime'
urlpatterns = [
    path('', Homepage.as_view(),name='homepage'),
    path('animes/', ListaAnimes.as_view(),name='animes'),
    path('episodios/', ListaEpisodios.as_view(),name='episodios'),
    path('animes/<int:pk>', DetalhesAnime.as_view(),name='detalhesAnime'),
    path('pesquisa/', PesquisaAnime.as_view(),name='pesquisaAnime'),
    path('perfil/', EditarPerfil.as_view(),name='editarPerfil'),
    path('cadastrar/', Cadastrar.as_view(),name='cadastrar'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    #path('animes/', include('anime.urls'))
]