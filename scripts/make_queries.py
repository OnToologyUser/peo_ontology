import os
from rdflib import Graph

rdf_file = os.path.join("..", "peo_ontology.rdf")

g = Graph()
g.parse(rdf_file, format="xml")