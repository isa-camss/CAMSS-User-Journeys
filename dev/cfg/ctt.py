# ctt.py
import cfg.sparql as sparql

CELLAR_CONNECTION = "http://publications.europa.eu/webapi/rdf/sparql"

URL_MICROSERVICE= 'http://localhost:5100/assessments/get_assessments'

TAB_NAMES_VALUES = [{'name':'Own queries', 'query_value':''}, 
                    {'name':'query 1', 'query_value':sparql.QUERY_ASSESSMENTS}, 
                    {'name':'query 2', 'query_value':sparql.QUERY_2}]
