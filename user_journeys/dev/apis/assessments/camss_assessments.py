from flask_restx import Namespace, Resource
from com.assessments.assessments import Assessments
import cfg.ctt as ctt
import com.util.io as io

api = Namespace("assessments", description="CAMSS Assessments")

assess_args = api.parser()
assess_args.add_argument('sparql_query',
                         required=True,
                         default='',
                         type=str,
                         help='Type the query to execute an sparql query throught CELLAR triplestore and '
                              'get information about CAMSS solutions')


@api.route('/ping')
class Ping(Resource):
    @api.doc("Returns 'pong' if invoked. Used to check that the NLP services are up and running.")
    def get(self):
        t0 = io.now()
        return {'message': f'pong ({str(io.now() - t0)})'}, 200


@api.route('/get_assessments')
class ApiAssessments(Resource):
    @api.doc(body="Obtains CAMSS assessments resources")
    @api.expect(assess_args)
    def post(self):
        """
        Main entry point to the API which produces all the artefacts for querying to the SPARQL end point of CELLAR
        Triplestore.
        """
        try:
            args = assess_args.parse_args()
            assess = Assessments(ctt.CELLAR_CONNECTION)
            msg = assess.get_assessment(args['sparql_query'])
            list_response = msg['results']['bindings']
            list_result_json = []

            for element_dict in list_response:
                dict_result = {}
                for key, value in element_dict.items():
                    dict_result[key] = value.get('value')
                list_result_json.append(dict_result)
            results_format = {'list_result': list_result_json}
            status_code = 201
        except Exception as ex:
            status_code = 555
            results_format = {"Error executing query. Exception: ": str(ex)}

        return results_format, status_code
