from flask import Flask
from apis.assessments import api
import cfg.ctt as ctt

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    app.run(port=ctt.API_PORT, debug=ctt.API_DEBUG)
