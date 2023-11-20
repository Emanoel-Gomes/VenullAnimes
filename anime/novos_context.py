from .models import Anime,Episodio


def lista_animes_recentes(requests):
    lista_animes = Anime.objects.all().order_by('-data_criacao')
    return {"lista_animes_recentes":lista_animes}

def lista_animes_emalta(requests):
    lista_animes = Anime.objects.all().order_by('-visualizacoes')
    return {"lista_animes_emalta":lista_animes}

def lista_episodios_recentes(requests):
    ista_episodios = Episodio.objects.all().order_by('-data_criacao')
    return {"lista_episodios_recentes": ista_episodios}