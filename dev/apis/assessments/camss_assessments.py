from flask_restx import Namespace, Resource
from com.assessments.assessments import Assessments
import cfg.ctt as ctt

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
        Main entry point to the GSF Thesaurus Re-indexation Pipeline, which produces all artifacts and sets the search
        up for working with the new thesauri.
        """
        args=assess_args.parse_args()
        assess = Assessments(ctt.CELLAR_CONNECTION)
        # t0 = io.now()
        msg = assess.get_assessment(args['sparql_query'])
        # io.log(f'Success: Process concluded. It took {io.now() - t0}')
        # msg['lapse'] = f'{str(io.now() - t0)})'
        return msg, 201
