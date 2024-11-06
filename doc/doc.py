from pylode.profiles.ontpub import OntPub

od = OntPub(ontology="../peo_ontology_ttl.ttl")

html = od.make_html()
od.make_html(destination="peo_ontology_doc.html")

print("Ontology documentation created successfully!")