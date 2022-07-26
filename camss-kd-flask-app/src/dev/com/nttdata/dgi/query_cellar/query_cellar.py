from SPARQLWrapper import SPARQLWrapper, JSON


class QueryCellar:
    url: str
    query: str

    def __init__(self, url_connection: str = None, sparql_query: str = None):
        self.url = url_connection
        self.query = sparql_query

    def get_query_results(self) -> dict:
        # Establish connection to cellar
        cellar_connection = SPARQLWrapper(self.url)

        # Execute query
        cellar_connection.setQuery(self.query)
        cellar_connection.setReturnFormat(JSON)
        cellar_response = cellar_connection.query().convert()

        # Format results
        list_response = cellar_response['results']['bindings']
        list_result_json = []
        for element_dict in list_response:
            dict_result = {}
            for key, value in element_dict.items():
                dict_result[key] = value.get('value')
            list_result_json.append(dict_result)
        results_format = {'list_result': list_result_json}

        return results_format
