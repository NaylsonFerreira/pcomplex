from django.http import JsonResponse
from .ontology import Ontology as Ontology_class
from django.shortcuts import render
from .models import Ontology


def index(request):
    tutorial = Ontology.objects.get(slug='PlayProfile')
    return render(request, "ontology_app/homepage.html", {'tutorial': tutorial})


def get_all_instances(request, ont_name, by_class):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    instances = ontology.get_instances_of(by_class)
    return JsonResponse(instances, safe=False)


def get_sub_class(request, ont_name, by_class):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    sub_classes = ontology.get_sub_classes_of(by_class)
    return JsonResponse(sub_classes, safe=False)


def get_tree_class(request, ont_name, by_class):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    sub_classes = ontology.get_sub_classes_of(by_class)
    tree = {}
    for branch in sub_classes:
        tree[branch] = ontology.get_sub_classes_of(branch)
    return JsonResponse(tree, safe=False)


def get_instance(request, ont_name, by_name):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    properties = ontology.get_instance(by_name)
    return JsonResponse(properties, safe=False)
