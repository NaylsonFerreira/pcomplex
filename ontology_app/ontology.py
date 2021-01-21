from owlready2 import *
from pcomplex_project.settings import BASE_DIR

class Ontology:
    dir_path = str(BASE_DIR) + "/ontology_app/ontologies/"
    file_name = ""
    path = dir_path+file_name
    onto_path.append(dir_path)
    base_iri = ""
    ontology = ""
    prefix = ""

    def __init__(self, file_name, prefix="myOnt"):
        self.file_name = file_name
        self.prefix = prefix
        self.load()
    
    def load(self):
        ontology = get_ontology(self.file_name)
        ontology.load()
        self.base_iri = ontology.base_iri
        self.ontology = ontology

    def query(self, query=""):
        set_import = "PREFIX "+self.prefix+": <"+self.base_iri+">\n"
        graph = default_world.as_rdflib_graph()
        query_SPARQL = set_import+query
        rows = list(graph.query(query_SPARQL))
        result = []
        for row in rows:
            replaced_row = []
            for term in row:
                replaced_row.append(str(term).replace(self.base_iri, ''))
            result.append(replaced_row)
        return result
    
    def get_instances_of(self,by_class):
        result = self.query("SELECT ?instances WHERE {?instances rdf:type "+self.prefix+":"+by_class+"}")
        instances = []
        for instance in result:
            instances += instance
        return instances
