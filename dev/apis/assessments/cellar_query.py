from SPARQLWrapper import SPARQLWrapper, JSON, CSV
from pprint import pprint
# from cfg.sparql import extract_assessments

if __name__ == '__main__':

    # Establish connection to cellar
    cellar_connection = SPARQLWrapper('http://publications.europa.eu/webapi/rdf/sparql')

    # Execute query
    # cellar_connection.setQuery(extract_assessments())
    cellar_connection.setQuery('''
                PREFIX camssa: <http://data.europa.eu/2sa/assessments/>
                PREFIX cssvrsc: <http://data.europa.eu/2sa/cssv/rsc/>
                PREFIX sc: <http://data.europa.eu/2sa/scenarios#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX cav: <http://data.europa.eu/2sa/cav#>
                PREFIX camss: <http://data.europa.eu/2sa#>
                PREFIX cssv: <http://data.europa.eu/2sa/cssv#>
                PREFIX dct: <http://purl.org/dc/terms/>
                select distinct ?Assessment ?Scenario
                where {
                    ?assObj rdf:type cav:Assessment ;
                    cav:contextualisedBy ?scObj ;
                    dct:title ?Assessment .
                    ?scObj rdf:type cav:Scenario ;
                    dct:title ?Scenario.
                    }
            ''')
    # Format results
    cellar_connection.setReturnFormat(JSON)
    qres = cellar_connection.query().convert()
    pprint(qres)
