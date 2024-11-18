import os
from rdflib import Graph

rdf_file = os.path.join("..", "peo_ontology.rdf")

g = Graph()
g.parse(rdf_file, format="xml")

# Query SPARQL
sparql_query = """
SELECT DISTINCT ?property ?value
WHERE {
    <https://w3id.org/peo#large_language_model> ?property ?value .
}
"""

# Esegui la query SPARQL
results = g.query(sparql_query)
for row in results:
    print(row)
