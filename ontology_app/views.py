from django.http import JsonResponse
from .ontology import Ontology as Ontology_class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Ontology
from rest_framework.decorators import api_view


def index(request):
    tutorial = Ontology.objects.get(slug='PlayProfile')
    return render(request, "ontology_app/homepage.html",
                  {'tutorial': tutorial})


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


@api_view(['POST', 'PUT'])
def create_or_update_instance(request, ont_name):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    payload = request.data
    try:
        ontology.add_instance(payload)
    except BaseException:
        pass
    properties = ontology.get_instance(payload['instance_name'])
    return JsonResponse(properties, safe=False)


@api_view(['DELETE'])
def delete_instance(request, ont_name, by_class, by_instance):
    ontology = Ontology.objects.get(slug=ont_name)
    ontology = Ontology_class(ontology.file.name)
    ontology.delete_instance(by_class, by_instance)
    ontology.get_instance(by_instance)
    return JsonResponse({})


class OntologyCreate(CreateView):
    model = Ontology
    fields = ['name', 'file']
    template_name = 'ontology_app/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Publicar nova Ontologia"
        return context


class OntologyList(ListView):
    model = Ontology
    paginate_by = 10


class OntologyDetail(DetailView):
    model = Ontology


class OntologyUpdate(UpdateView):
    model = Ontology
    exclude = ('user',)
    template_name = 'ontology_app/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Editar Ontologia"
        return context


class OntologyDelete(DeleteView):
    model = Ontology
    exclude = ('user',)
    template_name = 'ontology_app/form.html'
