# EXAMPLES
EXAMPLE_CELLAR_INPUT = '''
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

    select distinct ?Specification ?Assessment ?AssessmentLink where {

        ?CatalogRecords rdf:type dcat:CatalogRecord;
        foaf:primaryTopic ?PrimaryTopic;
        dct:title ?Specification.
        ?PrimaryTopic dct:relation ?relations.
        ?relations rdf:type cav:Assessment;
        dct:title ?Assessment.
        ?relations dcat:landingPage ?AssessmentLink.
    } 
    
    LIMIT 1000
    '''
