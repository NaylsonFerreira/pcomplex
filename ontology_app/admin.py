from django.contrib import admin
from .models import Ontology, OntologyAdmin

admin.site.register(Ontology, OntologyAdmin)
