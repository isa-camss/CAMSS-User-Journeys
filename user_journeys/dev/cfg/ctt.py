# ctt.py
import cfg.sparql as sparql

CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"

URL_MICROSERVICE = 'http://localhost:5100/assessments/get_assessments'

PROCURER_USE_CASES = [
    {'name': 'UC-1',
     'title': 'SPECIFICATIONS CATALOG',
     'query_value': sparql.QUERY_ALL_SPECIFICATIONS_ASSESSED,
     'description': '''This SPARQL query returns the interoperability specifications catalog by CAMSS and their 
      assessments. Press the Run button to execute it. You can also modify the query if you need to complement it'''},
    {'name': 'UC-2',
     'title': 'ONE SPECIFICATION ASSESSMENT',
     'query_value': '',
     'description': '''This SPARQL query re-directs the user to one Specification Assessment dataset and report. Press the Run button to execute it. You can also 
     modify the query if you need to complement it'''},
    {'name': 'UC-3',
     'title': '',
     'query_value': '',
     'description': '''Downloads one concrete scenario-based CAMSS Assessments. Press the Run button to execute it. You can also modify the query 
     if you need to complement it'''},
    {'name': "Custom queries",
     'title': '',
     'query_value': '',
     'description': '''In this section you can develop a SPARQL query of your own. Type the query in the textarea and press the Run button to
     execute it.'''}]

SOFTWARE_USE_CASES = [
    {'name': 'UC-1',
     'title': 'SPECIFICATIONS ASSOCIATED TO EIRA ABBs',
     'query_value': sparql.QUERY_SPECIFICATIONS_ASSESSED_ASSOCIATED_TO_EIRA_ABBS,
     'description': '''This SPARQL query returns the interoperability specifications assessed by CAMSS and associated to EIRA ABBs.
     Press the Run button to execute it. You can also modify the query if you need to complement it'''},
    {'name': 'UC-2',
     'title': 'ONE SPECIFICATION ASSESSMENT',
     'query_value': '',
     'description': '''This SPARQL query re-directs the user to one Specification Assessment dataset and report. Press the Run button to execute it. You can also 
     modify the query if you need to complement it'''},
    {'name': 'UC-3',
     'title': '',
     'query_value': '',
     'description': '''...'''},
    {'name': "Custom queries",
     'title': '',
     'query_value': '',
     'description': '''In this section you can develop a SPARQL query of your own. Type the query in the textarea and press the Run button to
     execute it.'''}]
