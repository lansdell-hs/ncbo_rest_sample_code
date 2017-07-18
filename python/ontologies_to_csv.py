import urllib2
import json
import ast
import csv

REST_URL = "http://data.bioontology.org"
API_KEY = "0640b94d-63f7-49f3-9be5-f79354797620"

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

acronyms=[]
names=[]
ontologies = get_json(REST_URL+"/ontologies")

ont = None
for ontology in ontologies:
    acronyms.append(ontology["acronym"])
    names.append(ontology["name"])

names_literal=ast.literal_eval(json.dumps(names))
acronyms_literal=ast.literal_eval(json.dumps(acronyms))

with open('ontologies.csv', 'w') as csvfile:
    for i, j in zip(acronyms_literal, names_literal):
        #print (i, j)
        ont_writer = csv.writer(csvfile)
        ont_writer.writerow([i,j])
