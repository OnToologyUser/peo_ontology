from pylode.profiles.ontpub import OntPub

od = OntPub(ontology="../peo_ontology_ttl.ttl")
od.make_html(destination="peo_ontology_doc.html")

print("\nOntology documentation created successfully!")