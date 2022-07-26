from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint
import config.constants as constants
from apis.api_microservices import blueprint as api
from flask_cors import CORS
from com.nttdata.utils.loggers import config_logging
import logging

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

swagger_url = constants.END_POINT_SWAGGER
swagger_ui_api_text = get_swaggerui_blueprint(base_url=swagger_url,
                                              api_url=constants.END_POINT_SWAGGER_JSON,
                                              blueprint_name=constants.NAME_BLUEPRINT)

app.register_blueprint(api)
app.register_blueprint(swagger_ui_api_text, url_prefix=swagger_url)

CORS(app)

config_logging()
logger = logging.getLogger(__name__)

# helpers.UsefulMethods().create_dirs()


@app.route("/")
def starting_url():
    return redirect(f"{constants.END_POINT_API}")
