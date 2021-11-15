QUERY_ASSESSMENTS = '''
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
    '''
