# url - view - template
from django.urls import path,include
from .views import Homepage,DetalhesAnime,ListaAnimes

app_name = 'anime'
urlpatterns = [
    path('', Homepage.as_view(),name='index'),
    path('animes/', ListaAnimes.as_view(),name='animes'),
    path('animes/<int:pk>', DetalhesAnime.as_view(),name='detalhesAnime'),
    #path('animes/', include('anime.urls'))
]