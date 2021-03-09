from django.contrib import admin
from .models import Ontology, OntologyAdmin, Jogo, JogoAdmin

admin.site.register(Ontology, OntologyAdmin)
admin.site.register(Jogo, JogoAdmin)
