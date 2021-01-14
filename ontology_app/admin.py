from django.contrib import admin
from .models import Perfil, Sujeito, Jogador, Jogo

admin.site.register({Perfil, Sujeito, Jogador, Jogo})
