from django.contrib import admin
from .models import Anime,Episodio,Genero,Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Informações pessoais",{'fields': ('animes_vistos','assistindo','assistir_depois','episodios_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)
# Register your models here.


admin.site.register(Anime)
admin.site.register(Episodio)
admin.site.register(Genero)
admin.site.register(Usuario, UserAdmin)