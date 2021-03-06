from SPARQLWrapper import SPARQLWrapper, JSON


class Assessments:

    def __init__(self, url_connection: str):
        self.url = url_connection

    def get_assessment(self, query: str) -> dict:
        # Establish connection to cellar
        cellar_connection = SPARQLWrapper(self.url)

        # Execute query
        cellar_connection.setQuery(query)
        
        # Format results
        cellar_connection.setReturnFormat(JSON)
        qres = cellar_connection.query().convert()

        return qres
