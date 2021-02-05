from django.http import HttpResponse, JsonResponse
from .ontology import Ontology
ontology = Ontology("PlayerProfile.owl")


def index(request):
    return HttpResponse("PyComplex")


def get_all_instances(request, by_class):
    instances = ontology.get_instances_of(by_class)
    return JsonResponse(instances, safe=False)


def get_sub_class(request, by_class):
    sub_classes = ontology.get_sub_classes_of(by_class)
    return JsonResponse(sub_classes, safe=False)


def get_tree_class(request, by_class):
    sub_classes = ontology.get_sub_classes_of(by_class)
    tree = {}
    for branch in sub_classes:
        tree[branch] = ontology.get_sub_classes_of(branch)
    return JsonResponse(tree, safe=False)


def get_instance(request, by_name):
    properties = ontology.get_instance(by_name)
    return JsonResponse(properties, safe=False)
