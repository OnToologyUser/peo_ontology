import os
from rdflib import Graph

rdf_file = os.path.join("..", "peo_ontology.rdf")

g = Graph()
g.parse(rdf_file, format="xml")

# Query SPARQL
sparql_query = """
SELECT ?llm  ?llmType ?company 
WHERE {
    # Retrieve companies
    ?company rdf:type <https://w3id.org/peo#company> .
    
    # Link companies to LLM instances through the develops relation
    ?company <https://w3id.org/peo#develops> ?llm .
    
    # Ensure the LLM is an instance of a subclass of LargeLanguageModel
    ?llm rdf:type ?llmType .
    ?llmType rdfs:subClassOf <https://w3id.org/peo#large_language_model> .
    
    # Optionally retrieve labels for companies, LLMs, and LLM types
    OPTIONAL { ?company rdfs:label ?companyLabel . }
    OPTIONAL { ?llm rdfs:label ?llmLabel . }
    OPTIONAL { ?llmType rdfs:label ?llmTypeLabel . }
}
"""

# Esegui la query SPARQL
results = g.query(sparql_query)
for row in results:
    print(row)
