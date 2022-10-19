import config.sparql as sparql
import os

# -------------------------------------------- PROJECT CONFIGURATION -------------------------------------------------
PROJECT_NAME = 'camss-knowledge-discovery'
PROJECT_VERSION = 'v1'

# ---------------------------------------------- BACKEND CONNECTION -------------------------------------------------
API_NAME = 'api-cellar-queries'
API_VERSION = 'v1'
API_TITLE = 'CELLAR'
END_POINT_NAME = 'query'

# -------------------------------------------- DOCKER CONFIGURATION -------------------------------------------------

FLASK_HOST_PORT = os.environ.get('FLASK_HOST_PORT') if os.environ.get('FLASK_HOST_PORT') else 'http://127.0.0.1:5000'
URL_MICROSERVICE = f'{FLASK_HOST_PORT}/api-cellar-queries/v1/CELLAR/query'

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
