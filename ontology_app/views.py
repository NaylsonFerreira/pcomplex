# from django.shortcuts import render
from django.http import HttpResponse
# from .models import *
from owlready2 import *
from pcomplex_project.settings import BASE_DIR


def index(request):
    path = str(BASE_DIR)+"/ontology_app/ontologies"
    onto_path.append(path)
    player_profile = get_ontology("PlayerProfile.owl")
    player_profile.load()
    sync_reasoner()
    return HttpResponse("player_profile")
