import os

# -------------------------------------------- PROJECT CONFIGURATION -------------------------------------------------
PROJECT_NAME = 'api-cellar-queries'
VERSION = 'v1.0'
PROJECT_NAME_FOLDER = 'dev'
BASE_PATH_EXECUTE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_PATH = os.path.dirname(BASE_PATH_EXECUTE)
HOME_PATH_LOG = os.path.join(BASE_PATH, PROJECT_NAME_FOLDER, 'logs')

# ----------------------------------------------- API CONFIGURATION -------------------------------------------------
# API INFO
NAME_API = 'cellarQueries'
TITLE_API = 'cellarQueries.API - Development'
DESCRIPTION_API = 'This microservice is responsible for querying CELLAR Triplestore.'
NAME_BLUEPRINT = 'cellar_queries_blueprint'
API_PORT = 5000
API_DEBUG = False

# API GENERIC URL
END_POINT_API = f'/{PROJECT_NAME}/{VERSION[:2]}'
END_POINT_SWAGGER = f'{END_POINT_API}/swagger'
END_POINT_SWAGGER_JSON = f'{END_POINT_API}/swagger.json'

# API KEYS
KEY_TITLE = 'title'
KEY_TITLE_END_POINT = 'end_point'
KEY_TITLE_DIRECTORIES = 'directories'
KEY_DESCRIPTION = 'description'
KEY_DOC = 'documentation'

# API KEYS ENDPOINTS
KEY_CELLAR = 'cellar'

# TITLES
TITLE_CELLAR = 'CELLAR'

# DESCRIPTIONS
DESCRIPTION_TEMPLATE_1 = 'API namespace for querying CELLAR Triplestore'

DESCRIPTION_CELLAR_MODEL_INPUT = 'Input designed to receive an string with query.'
DESCRIPTION_TEMPLATE_MODEL_OUTPUT_RESULT = 'String output resulting of the process'

DESCRIPTION_TEMPLATE_1_TYPE = 'Int indicating the type of request.'
DESCRIPTION_TEMPLATE_1_MESSAGE = 'String indicating the result in text.'

# DOCUMENTATION
DOCUMENTATION_TEMPLATE_1 = 'Class to execute the fibuzz class that returns "Fizz" when getting numbers divisible by ' \
                           '3, "Buzz" when getting numbers divisible by 5 or "FizzBuzz" when getting a number ' \
                           'divisible by 3 and 5.Used to check that the services are up and running. '

# ENDPOINTS
END_POINT_TEMPLATE_1 = "/query"

# KEY ARGUMENTS
KEY_NAME_QUERY = 'query'
KEY_NAME_RESPONSE_MESSAGE = 'message'
KEY_NAME_RESPONSE_RESULT = 'result'
KEY_NAME_RESPONSE = 'response'

# -------------------------------------------- FUNCTIONALITIES -------------------------------------------------------

FUNCTIONALITIES = {
    KEY_CELLAR: {KEY_TITLE: TITLE_CELLAR, KEY_TITLE_END_POINT: END_POINT_TEMPLATE_1, KEY_TITLE_DIRECTORIES: [],
                 KEY_DESCRIPTION: DESCRIPTION_TEMPLATE_1, KEY_DOC: DOCUMENTATION_TEMPLATE_1}
}

# ------------------------------------------------- CELLAR -----------------------------------------------------------
CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"
