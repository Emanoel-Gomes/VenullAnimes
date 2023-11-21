# url - view - template
from django.urls import path,include
from .views import Homepage,DetalhesAnime,ListaAnimes,PesquisaAnime

app_name = 'anime'
urlpatterns = [
    path('', Homepage.as_view(),name='homepage'),
    path('animes/', ListaAnimes.as_view(),name='animes'),
    path('animes/<int:pk>', DetalhesAnime.as_view(),name='detalhesAnime'),
    path('pesquisa/', PesquisaAnime.as_view(),name='pesquisaAnime'),
    #path('animes/', include('anime.urls'))
]