from SPARQLWrapper import SPARQLWrapper, JSON,CSV
from pprint import pprint
# impor cfg.sparql

class Assessments:
    # def __init__(self, con_string):
    #   self.connection_string = con_string

    def get_assessment(self):

        # Establish connection to cellar
        cellar_connection = self.SPARQLWrapper('http://publications.europa.eu/webapi/rdf/sparql')

        # Execute query
        cellar_connection.setQuery(QUERY_ASSESSMENTS)
        # Format results
        cellar_connection.setReturnFormat(JSON)
        qres = cellar_connection.query().convert()

        pprint(qres)

        # return {"msg": "success"}, 201
