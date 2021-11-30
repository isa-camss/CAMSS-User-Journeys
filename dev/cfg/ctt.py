# ctt.py
import cfg.sparql as sparql

CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"

URL_MICROSERVICE = 'http://localhost:5100/assessments/get_assessments'

TAB_VALUES = [
    {'name': 'Own queries', 'query_value': '', 'description': 'In this section you can make a SPARQL query of '
                                                              'whatever you want to Cellar Triplestore. Type '
                                                              'the query in the textarea and press the Run '
                                                              'button to execute it.'},
    {'name': 'query 1', 'query_value': sparql.QUERY_ASSESSMENTS, 'description': 'In this query SPARQL returns all the '
                                                                                'assessments and their scenarios. '
                                                                                'Press the Run button to execute it. '
                                                                                'You can also modify the query if you '
                                                                                'need to complement it'},
    {'name': 'query 2', 'query_value': sparql.QUERY_2, 'description': 'This SPARQL query is a test. Press the Run '
                                                                      'button to execute it. You can also modify the '
                                                                      'query if you need to complement it'}]
