from django.urls import path
from .views import index

app_name = 'ontology_app'
urlpatterns = [
    path('', index, name="Index"),
]
