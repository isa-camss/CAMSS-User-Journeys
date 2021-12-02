# ctt.py
import cfg.sparql as sparql

CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"

URL_MICROSERVICE = 'http://localhost:5100/assessments/get_assessments'

TAB_VALUES = [
    {'name': 'UC1: Specs Catalog', 
     'query_value': sparql.QUERY_ALL_SPECIFICATIONS_ASSESSED, 
     'description':'''This SPARQL query returns the interoperability specifications catalog by CAMSS and their 
      assessments. Press the Run button to execute it. You can also modify the query if you need to complement it''' },
    {'name': 'UC2: One Specification Assessement', 
     'query_value': '', 
     'description': '''Re-directs the user to one Specification Assessment dataset and report. Press the Run button to execute it. You can also 
     modify the query if you need to complement it'''},
    {'name': 'UC3: Scenario-based Assessement', 
     'query_value': '', 
     'description': '''Downloads one concrete scenario-based CAMSS Assessments. ress the Run button to execute it. You can also modify the query 
     if you need to complement it'''},
    {'name': "Custom queries", 
     'query_value': '', 
     'description': '''In this section you can develop a SPARQL query of your own. Type the query in the textarea and press the button to execute 
     it.'''}]
