from flask_restx import Namespace, Resource
from com.assessments.assessments import Assessments
import cfg.ctt as ctt
import pandas as pd
import json

api = Namespace("assessments", description="CAMSS Assessments")

assess_args = api.parser()
assess_args.add_argument('sparql_query', required=True, default='', type=str,
                         help='Type the query to execute an sparql query throught CELLAR triplestore and get information '
                              'about CAMSS solutions')


@api.route('/get_assessments')
@api.expect(assess_args)
class ApiAssessments(Resource):
    @api.doc(body="Obtains CAMSS assessments resources")
    def post(self):
        """
        Main entry point to the API which produces all the artefacts for querying to the SPARQL end point of CELLAR
        Triplestore.
        """
        args = assess_args.parse_args()
        assess = Assessments(ctt.CELLAR_CONNECTION)
        # t0 = io.now()
        msg = assess.get_assessment(args['sparql_query'])
        # io.log(f'Success: Process concluded. It took {io.now() - t0}')
        # msg['lapse'] = f'{str(io.now() - t0)})'
        results_format = msg['results']['bindings']
        '''
        assessments_list = []
        scenario_list = []
        
        for item_list in results_format:
            assessment_value = item_list['Assessment']['value']
            assessments_list.append(assessment_value)

            scenario_value = item_list['Scenario']['value']
            scenario_list.append(scenario_value)

        results = {'Assessments': assessments_list, 'Scenario': scenario_list}
        df_assessments = pd.DataFrame(results, columns=['Assessments', 'Scenario'])
        '''

        print(results_format)

        return results_format, 201
