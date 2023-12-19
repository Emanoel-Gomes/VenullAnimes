from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
#Generos (tupla); a primeira parte é o que será armazenado no bd
#e o segundo é o nome que irá aparecer

LISTA_GENEROS = (
    ("ACAO","Ação"),
    ("ARTES_MARCIAIS","Artes Marciais"),
    ("AVENTURA","Aventura"),
    ("COMEDIA","Comédia"),
    ("DEMONIOS","Demônios"),
    ("DRAMA","Drama"),
    ("ECCHI","Ecchi"),
    ("ESCOLAR","Escolar"),
    ("ESPORTES","Esportes"),
    ("FANTASIA","Fantasia"),
    ("FICCAO_CIENTIFICA","Ficção Científica"),
    ("HAREM","Harém"),
    ("HISTORICO","Histórico"),
    ("HORROR","Horror"),
    ("JOGO","Jogo"),
    ("LIGHT_NOVEL","Light Novel"),
    ("MAGIA","Magia"),
    ("MECHA","Mecha"),
    ("MILITAR","Militar"),
    ("MISTERIO","Mistério"),
    ("MUSICAL","Musical"),
    ("ROMANCE","Romance"),
    ("SAMURAI","Samurai"),
    ("SEINEN","Seinen"),
    ("SEM_CENSURA","Sem Censura"),
    ("SHOUJO","Shoujo"),
    ("SHOUNEN","Shounen"),
    ("SLICE_OF_LIFE","Slice of Life"),
    ("SOBRENATURAL","Sobrenatural"),
    ("SUPER_PODERES","Super Poderes"),
    ("SUSPENSE","Suspense"),
    ("TERROR","Terror"),
    ("YAOI","Yaoi"),
    ("YURI","Yuri"),
)

DIAS_SEMANA = (
    ("SEGUNDA","Segunda"),
    ("TERCA","Terca"),
    ("QUARTA","Quarta"),
    ("QUINTA","Quinta"),
    ("SEXTA","Sexta"),
    ("SABADO","Sabado"),
    ("DOMINGO","Domingo"),
)


LISTA_CLASSIFICACOES = (
    (10,10),
    (12,12),
    (14,14),
    (16,16),
    (18,18),

)

LISTA_TEMPORADAS = (
    ("INVERNO","Inverno"),
    ("PRIMAVERA","Primavera"),
    ("VERAO","Verão"),
    ("OUTONO","Outono"),
)

LISTA_TIPO = (
    ("LEGENDADO", "Legendado"),
    ("DUBLADO","Dublado")
)

class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=1000)
    classificacao = models.IntegerField(choices=LISTA_CLASSIFICACOES)
    distribuidora = models.CharField(max_length=50)
    thumb = models.ImageField(upload_to='thumb_animes')
    tipo = models.CharField(max_length=10, choices=LISTA_TIPO)
    temporada = models.CharField(max_length=10, choices=LISTA_TEMPORADAS)
    dia_semana = models.CharField(default="SEGUNDA", max_length=8, choices=DIAS_SEMANA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# Episódios
class Episodio(models.Model):
    anime = models.ForeignKey("Anime", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    data_criacao = models.DateTimeField(default=timezone.now)
    thumb_episodio = models.ImageField(upload_to='thumb_episodios', default='default_thumb.jpg')
    
    def __str__(self):
        return self.titulo
    

# Generos
class Genero(models.Model):
    anime = models.ForeignKey("Anime", related_name="generos", on_delete=models.CASCADE)
    generos = models.CharField(max_length=18, choices=LISTA_GENEROS)
    
    def __str__(self):
        return self.generos
    
class Usuario(AbstractUser):
    animes_vistos = models.ManyToManyField("Anime", related_name="animes_vistos")
    assistir_depois = models.ManyToManyField("Anime", related_name="assistir_depois")
    assistindo = models.ManyToManyField("Anime", related_name="assistindo")
    episodios_vistos = models.ManyToManyField("Episodio")
    
