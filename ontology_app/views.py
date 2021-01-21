# from django.shortcuts import render
from django.http import HttpResponse
# from .models import *
from .ontology import Ontology


def index(request):
    ontology = Ontology("PlayerProfile.owl")
    players = ontology.get_instances_of("Jogador")
    jogos = ontology.get_instances_of("Jogo")
    print(players)
    return HttpResponse(players)
