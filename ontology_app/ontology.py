from owlready2 import onto_path, sync_reasoner, get_ontology, default_world
from pcomplex_project.settings import ONTOLOGIES_DIR


class Ontology:
    dir_path = str(ONTOLOGIES_DIR)
    file_name = ""
    path = dir_path + file_name
    onto_path.append(dir_path)
    base_iri = ""
    ontology = ""
    prefix = ""

    def __init__(self, file_name, prefix="myOnt"):
        self.file_name = file_name
        self.prefix = prefix
        self.load()
        try:
            sync_reasoner()
        except BaseException:
            pass

    def load(self):
        ontology = get_ontology(self.file_name)
        ontology.load()
        self.base_iri = ontology.base_iri
        self.ontology = ontology

    def query(self, query="", show_print=False):
        set_import = """
        PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl:  <http://www.w3.org/2002/07/owl#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
        PREFIX %s:   <%s> \n
        """ % (self.prefix, self.base_iri)
        graph = default_world.as_rdflib_graph()
        query_SPARQL = set_import + query
        if show_print:
            print(query_SPARQL)
        rows = list(graph.query(query_SPARQL))
        result = []
        for row in rows:
            replaced_row = []
            for term in row:
                replaced_row.append(str(term).replace(self.base_iri, ''))
            result.append(replaced_row)
        return result

    def get_instances_of(self, by_class):
        query = """
        SELECT  ?instances
        WHERE {
                ?instances rdf:type owl:NamedIndividual .
                ?instances rdf:type %s:%s
            }
        """ % (self.prefix, by_class)
        result = self.query(query)
        instances = []
        for instance in result:
            instances += instance
        return instances

    def get_sub_classes_of(self, by_class):
        query = """
        SELECT ?instances
        WHERE {
                ?instances rdfs:subClassOf* %s:%s
            }
        """ % (self.prefix, by_class)
        result = self.query(query)
        instances = []
        for instance in result:
            instances += instance
        return instances

    def get_instance(self, by_name):
        query_properties = """
        SELECT  ?properties ?values
        WHERE {
            %s:%s rdf:type ?all_types .
            ?all_types owl:onProperty ?properties .
            ?all_types owl:someValuesFrom ?values
        }
        """ % (self.prefix, by_name)
        result_properties = self.query(query_properties)
        properties = []
        for row in result_properties:
            properties.append(row[0] + " " + row[1])

        query_class = """
        SELECT  ?classes
        WHERE {
            %s:%s rdf:type ?classes .
            ?classes rdf:type owl:Class
        }
        """ % (self.prefix, by_name)
        result_class = self.query(query_class)
        classes = []
        for row in result_class:
            classes += row

        return classes + properties
