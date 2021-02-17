from django.urls import path
from django.contrib.auth.decorators import login_required
from ontology_app import views

app_name = 'ontology_app'
urlpatterns = [
    path('', views.index, name="Index"),

    path('subclasses/<str:ont_name>/<str:by_class>/',
         views.get_sub_class,
         name="Subclasses"),

    path('tree/<str:ont_name>/<str:by_class>/',
         views.get_tree_class,
         name="Tree"),

    path('instances/<str:ont_name>/<str:by_class>/',
         views.get_all_instances,
         name="Instances"),

    path('instance/<str:ont_name>/<slug:by_name>/',
         views.get_instance,
         name="Instance"),

    path('add/instance/<str:ont_name>/',
         views.create_or_update_instance,
         name="AddInstance"),

    path('delete/instance/<str:ont_name>/<str:by_class>/<str:by_instance>/',
         views.delete_instance,
         name="DeleteInstance"),

    path('ontologies/',
         login_required(views.OntologyList.as_view()), name='OntologyList'),

    path('ontology/<int:pk>/',
         login_required(views.OntologyDetail.as_view()), name='OntologyDetail'),

    path('ontology/add/',
         login_required(views.OntologyCreate.as_view()), name='OntologyCreate'),

    path('ontology/up/<int:pk>/',
         login_required(views.OntologyUpdate.as_view()), name='OntologyUpdate'),

    path('ontology/del/<int:pk>/',
         login_required(views.OntologyDelete.as_view()), name='OntologyDelete'),

]
