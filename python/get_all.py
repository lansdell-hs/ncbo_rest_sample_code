import urllib2
import json

REST_URL = "http://data.bioontology.org"
API_KEY = "0640b94d-63f7-49f3-9be5-f79354797620"


def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

# Get all ontologies from the REST service and parse the JSON
ontologies = get_json(REST_URL+"/ontologies")

# Iterate looking for ontology with acronym BRO
ont = None
for ontology in ontologies:
    if ontology["acronym"] == "BRO":
        ont = ontology

labels = []
synonyms=[]
definitions=[]
#semantics=[]
links_per_term=[]
# Using the hypermedia link called `classes`, get the first page
page = get_json(ont["links"]["classes"])

# Iterate over the available pages adding labels from all classes
# When we hit the last page, the while loop will exit
next_page = page
while next_page:
    next_page = page["links"]["nextPage"]
    for ont_class in page["collection"]:
        labels.append(ont_class["prefLabel"])
        synonyms.append(ont_class["synonym"])
        definitions.append(ont_class["definition"])
 #       semantics.append(ont_class["semanticType"])
        links_per_term.append(ont_class["links"])


    if next_page:
        page = get_json(next_page)

# Output the labels
#for label in labels:
 #   print label
#for synonym in synonyms:
 #   print synonym
#for definition in definitions:
 #   print definition
#for semantic in semantics:
 #   print semantic
for link in links_per_term:
    print link
    print ""
