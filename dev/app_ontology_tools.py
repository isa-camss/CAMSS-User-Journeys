from flask import Flask
from apis.assessments import api

"""LOG_FILE = './log/govs.log'
io.make_file_dirs(LOG_FILE)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
level=logging.INFO, filename=LOG_FILE)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
logger = logging.getLogger("govs")
logger.setLevel(level=logging.WARNING)"""

app = Flask(__name__)
api.init_app(app)
# app.logger = logger

if __name__ == '__main__':
    # print(f'Log level set to {logger.level}')
    app.run(port='5100', debug=True)
