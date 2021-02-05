from django.urls import path
from .views import index, get_all_instances, get_sub_class, get_tree_class, get_instance

app_name = 'ontology_app'
urlpatterns = [
    path('', index, name="Index"),
    path('subclasses/<str:by_class>/', get_sub_class, name="Subclasses"),
    path('tree/<str:by_class>/', get_tree_class, name="Tree"),

    path('instances/<str:by_class>/', get_all_instances, name="Instances"),
    path('instance/<slug:by_name>', get_instance, name="Instance"),
]
