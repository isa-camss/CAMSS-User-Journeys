from SPARQLWrapper import SPARQLWrapper, JSON, CSV
from pprint import pprint
import cfg.sparql as sparql


class Assessments:

    def __init__(self, url_connection: str):
        self.url = url_connection

    def get_assessment(self) -> dict:
        # Establish connection to cellar
        cellar_connection = SPARQLWrapper(self.url)

        # Execute query
        cellar_connection.setQuery(sparql.QUERY_ASSESSMENTS)
        # Format results
        cellar_connection.setReturnFormat(JSON)
        qres = cellar_connection.query().convert()
        return qres

        # pprint(qres)

        # return {"msg": "success"}, 201
