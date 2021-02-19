from owlready2 import onto_path, sync_reasoner, get_ontology, default_world, destroy_entity
from pcomplex_project.settings import MEDIA_URL


class Ontology():
    dir_path = MEDIA_URL
    file_name = ""
    path = ""
    onto_path.append(dir_path)
    base_iri = ""
    ontology = ""
    prefix = ""

    def __init__(self, file_name, prefix="myOnt"):
        self.file_name = file_name
        self.path = self.dir_path + self.file_name
        self.prefix = prefix
        self.load()

    def load(self):
        ontology = get_ontology(self.path)
        ontology.load()
        self.base_iri = ontology.base_iri
        self.ontology = ontology
        try:
            sync_reasoner()
        except BaseException:
            pass

    def query(self, query="", show_print=False):
        self.load()
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

        try:
            query_class = """
            SELECT DISTINCT ?games
            WHERE {
                %s:%s rdf:type ?all_types .
                ?all_types owl:someValuesFrom ?habilidades .

                ?habilidades rdfs:subClassOf myOnt:Habilidade .
                ?habilidades rdfs:subClassOf ?Habtypes .
                ?Habtypes owl:someValuesFrom ?sujeitos .

                ?games rdf:type myOnt:Jogo .
                ?games rdf:type owl:NamedIndividual .
                ?games rdf:type ?gamesTypes .
                ?gamesTypes owl:someValuesFrom ?sujeitos .
            }
            """ % (self.prefix, by_name)
            result_games = self.query(query_class)
            games = []
            for row in result_games:
                games += row
        except BaseException:
            games = {}

        return {'classes': classes, 'properties': properties, 'games': games}

    def add_instance(self, payload):
        class_name = payload['class_name']
        instance_name = payload['instance_name']
        property_name = payload['property_name']
        property_values = payload['property_values']

        onto_file = self.ontology
        onto_class = self.ontology[class_name]
        onto_property = self.ontology[property_name]

        try:
            new_instance = onto_class(instance_name, namespace=onto_file)
            destroy_entity(new_instance)
            new_instance = onto_class(instance_name, namespace=onto_file)
            for value in property_values:
                onto_value = self.ontology[value]
                new_instance.is_a.append(onto_property.some(onto_value))
            onto_file.save(self.path)
            self.load()
        except BaseException:
            pass

    def delete_instance(self, class_name, instance_name):
        onto_file = self.ontology
        onto_class = self.ontology[class_name]

        try:
            new_instance = onto_class(instance_name, namespace=onto_file)
            destroy_entity(new_instance)
            onto_file.save(self.path)
            self.load()
        except BaseException:
            pass
