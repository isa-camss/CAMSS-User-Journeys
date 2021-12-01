# ctt.py
import cfg.sparql as sparql

CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"

URL_MICROSERVICE = 'http://localhost:5100/assessments/get_assessments'

TAB_VALUES = [
    {'name': "Custom queries", 
     'query_value': '', 
     'description': '''In this section you can make a SPARQL query of whatever you want to Cellar Triplestore.br &nbsp; 
      Type the query in the textarea and press the button to execute it.'''},
    {'name': 'UC1: Specs Catalog', 
     'query_value': sparql.QUERY_ALL_SPECIFICATIONS_ASSESSED, 
     'description':'''This SPARQL query returns the interoperability specifications catalog by CAMSS and their 
      assessments. Press the Run button to execute it. You can also modify the query if you need to complement it''' },
    {'name': 'UC2: EIRA ABBs', 
     'query_value': sparql.QUERY_SPECIFICATIONS_ASSESSED_ASSOCIATED_TO_EIRA_ABBS, 
     'description': '''This SPARQL query, given one or more ABBs get the specifications linked to that ABBs. Press the 
      Run button to execute it. You can also modify the query if you need to complement it'''}]
