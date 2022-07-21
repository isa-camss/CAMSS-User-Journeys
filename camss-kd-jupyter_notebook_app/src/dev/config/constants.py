import config.sparql as sparql

# -------------------------------------------- PROJECT CONFIGURATION -------------------------------------------------
PROJECT_NAME = 'camss-knowledge-discovery'
PROJECT_VERSION = 'v1'

# ---------------------------------------------- BACKEND CONNECTION -------------------------------------------------
API_NAME = 'api-cellar-queries'
API_VERSION = 'v1'
API_TITLE = 'CELLAR'
END_POINT_NAME = 'query'
API_PORT = 5000
API_DEBUG = False
END_POINT_MICROSERVICE = f'http://localhost:{API_PORT}/{API_NAME}/{API_VERSION}/{API_TITLE}/{END_POINT_NAME}'
URL_MICROSERVICE = 'http://localhost:5000/api-cellar-queries/v1/CELLAR/query'

# ---------------------------------------------- CELLAR CONNECTION -------------------------------------------------
CELLAR_CONNECTION = 'http://publications.europa.eu/webapi/rdf/sparql'

# -------------------------------------------------- USE CASES -------------------------------------------------------
PROCURER_USE_CASES = [
    {'name': 'Step 1',
     'title': '<strong>SPECIFICATIONS CATALOG</strong>',
     'query_value': sparql.QUERY_ALL_SPECIFICATIONS_ASSESSED,
     'description': '''This SPARQL query returns the interoperability specifications catalog by CAMSS and their 
      assessments. You can also modify the query if you need to complement it.<br>Press the Run button to execute it.'''},
    {'name': "Custom queries",
     'title': '<strong>CUSTOM QUERIES</strong>',
     'query_value': '',
     'description': '''In this section you can develop a SPARQL query of your own.<br>Type the query in the textarea and press the Run button to
     execute it.'''}]

SOFTWARE_USE_CASES = [
    {'name': 'Step 1',
     'title': '<strong>SPECIFICATIONS ASSOCIATED TO EIRA ABBs</strong>',
     'query_value': sparql.QUERY_SPECIFICATIONS_ASSESSED_ASSOCIATED_TO_EIRA_ABBS,
     'description': '''This SPARQL query returns the interoperability specifications assessed by CAMSS and associated to EIRA ABBs.
     You can also modify the query if you need to complement it.<br>Press the Run button to execute it.'''},
    {'name': "Custom queries",
     'title': '<strong>CUSTOM QUERIES</strong>',
     'query_value': '',
     'description': '''In this section you can develop a SPARQL query of your own.<br>Type the query in the textarea and press the Run button to
     execute it.'''}]
