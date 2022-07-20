from flask import request
from apis.cellar_queries import logger
from com.nttdata.utils.helpers import UsefulMethods
from flask_restx import Namespace, Resource, fields
from com.nttdata.dgi.query_cellar.query_cellar import QueryCellar
from config import messages, constants, constants_examples

api = Namespace(constants.FUNCTIONALITIES[constants.KEY_CELLAR][constants.KEY_TITLE],
                description=constants.FUNCTIONALITIES[constants.KEY_CELLAR][constants.KEY_DESCRIPTION])

""" Input data model definition """
cellar_input = api.model('InputCellar', {
    constants.KEY_NAME_QUERY: fields.String(description=constants.DESCRIPTION_CELLAR_MODEL_INPUT,
                                            required=True,
                                            example=constants_examples.EXAMPLE_CELLAR_INPUT)
})

assess_args = api.parser()


@api.route(constants.FUNCTIONALITIES[constants.KEY_CELLAR][constants.KEY_TITLE_END_POINT])
class Cellar(Resource):
    @api.doc(constants.FUNCTIONALITIES[constants.KEY_CELLAR][constants.KEY_DOC])
    @api.expect(cellar_input, validate=True)
    @api.response(200, messages.MESSAGE_200)
    @api.response(400, messages.MESSAGE_400)
    @api.response(404, messages.MESSAGE_404)
    @api.response(500, messages.MESSAGE_500)
    def post(self):
        """
        Main entry point to the API which produces all the artefacts for querying to the SPARQL end point of CELLAR
        Triplestore.
        """
        try:
            t0 = UsefulMethods.now()
            logger.info(f'Received: {t0}')
            json_in = request.json
            assess = QueryCellar(constants.CELLAR_CONNECTION)
            msg = assess.get_assessment((json_in.get('query')))
            # args = assess_args.parse_args()
            # msg = assess.get_assessment(args['sparql_query'])
            list_response = msg['results']['bindings']
            list_result_json = []

            for element_dict in list_response:
                dict_result = {}
                for key, value in element_dict.items():
                    dict_result[key] = value.get('value')
                list_result_json.append(dict_result)
            results_format = {'list_result': list_result_json}
            status_code = 201
            return results_format, status_code
        except Exception as ex:
            status_code = 555
            results_format = {"Error executing query. Exception: ": str(ex)}

        return results_format, status_code
