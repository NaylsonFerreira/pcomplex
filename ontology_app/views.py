from django.http import HttpResponse, JsonResponse
from .ontology import Ontology
ontology = Ontology("PlayerProfile.owl")

def index(request):    
    players = ontology.get_instances_of("Jogador")
    jogos = ontology.get_instances_of("Jogo")
    return HttpResponse(players)


def get_all_instances(request, by_class):
    instances = ontology.get_instances_of(by_class)
    return JsonResponse(instances, safe=False)


def get_sub_class(request, by_class):
    sub_classes = ontology.get_sub_classes_of(by_class)
    return JsonResponse(sub_classes, safe=False)
