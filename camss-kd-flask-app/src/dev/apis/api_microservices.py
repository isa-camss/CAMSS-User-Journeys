from flask import Blueprint
from flask_restx import Api
import config.constants as constants

# APIs
from apis.cellar_queries.namespace_cellar_queries import api as cellar_api

blueprint = Blueprint(name=constants.NAME_API, import_name=__name__, url_prefix=constants.END_POINT_API)
api = Api(blueprint,
          title=constants.TITLE_API,
          version=constants.VERSION,
          description=constants.DESCRIPTION_API
          )

# API 1
api.add_namespace(cellar_api)

