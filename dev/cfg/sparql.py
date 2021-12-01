QUERY_ALL_SPECIFICATIONS_ASSESSED = '''
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix geo: <http://www.opengis.net/ont/geosparql#>
    prefix foaf: <http://xmlns.com/foaf/0.1/>
    prefix skos: <http://www.w3.org/2004/02/skos/core#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix camssa: <http://data.europa.eu/2sa/assessments/>
    prefix cav: <http://data.europa.eu/2sa/cav#>
    prefix cssv: <http://data.europa.eu/2sa/cssv#>
    prefix cssvrsc: <http://data.europa.eu/2sa/cssv/rsc/>
    prefix dcat: <http://www.w3.org/ns/dcat#>
    prefix dct: <http://purl.org/dc/terms#>
    prefix eira: <http://data.europa.eu/dr8#>
    prefix elis: <http://data.europa.eu/2sa/elis#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    select distinct ?TitleSpecification ?AssessmentTitle where {

        ?CatalogRecords rdf:type dcat:CatalogRecord;
        foaf:primaryTopic ?PrimaryTopic;
        dct:title ?TitleSpecification.
        ?PrimaryTopic dct:relation ?relations.
        ?relations rdf:type cav:Assessment;
        dct:title ?AssessmentTitle

    } 
    
    LIMIT 1000
    '''

QUERY_SPECIFICATIONS_ASSESSED_ASSOCIATED_TO_EIRA_ABBS = '''
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix geo: <http://www.opengis.net/ont/geosparql#>
    prefix foaf: <http://xmlns.com/foaf/0.1/>
    prefix skos: <http://www.w3.org/2004/02/skos/core#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix camssa: <http://data.europa.eu/2sa/assessments/>
    prefix cav: <http://data.europa.eu/2sa/cav#>
    prefix cssv: <http://data.europa.eu/2sa/cssv#>
    prefix cssvrsc: <http://data.europa.eu/2sa/cssv/rsc/>
    prefix dcat: <http://www.w3.org/ns/dcat#>
    prefix dct: <http://purl.org/dc/terms#>
    prefix eira: <http://data.europa.eu/dr8#>
    prefix elis: <http://data.europa.eu/2sa/elis#>
    prefix owl: <http://www.w3.org/2002/07/owl#>

    select distinct ?PrimaryTopic ?relation2 ?relation where {

    ?PrimaryTopic dct:relation ?relation2.{
        
        SELECT ?PrimaryTopic ?relation {
        ?CatalogRecords rdf:type dcat:CatalogRecord;
        foaf:primaryTopic ?PrimaryTopic.
        ?PrimaryTopic dct:title ?Specification.
        ?PrimaryTopic dct:relation ?relation.

        FILTER( contains(STR(?relation), "http://data.europa.eu/2sa/assessments/") )
        }
    }
    FILTER( contains(STR(?relation2), "http://data.europa.eu/dr8#") )
    }
    ORDER BY ?PrimaryTopic
    
    LIMIT 1000
    '''