from flask_restx import Namespace, Resource
from com.assessments import Assessments
import cfg.ctt as ctt

api = Namespace("Assessments", description="CAMSS Assessments")

ass_args = api.parser()
ass_args.add_argument('operation_code', required=True, default='BR-M1113', type=str,
                      help='Type the operation code of the resource whose wordcloud you want to find. Take into account'
                           " that if you want to find the wordcloud of a document, "
                           "you need to type in the resource_id parameter.")


@api.route('/get_assessments')
class ApiAssessments(Resource):
    @api.doc(body="Obtains CAMSS assessments resources")
    def post(self):
        """
        Main entry point to the GSF Thesaurus Re-indexation Pipeline, which produces all artifacts and sets the search up for working with the new thesauri.
        """
        asse = Assessments(ctt.CELLAR_CONNECTION)
        # t0 = io.now()
        msg, code = asse.get_assessment()
        # io.log(f'Success: Process concluded. It took {io.now() - t0}')
        # msg['lapse'] = f'{str(io.now() - t0)})'
        return msg, code
