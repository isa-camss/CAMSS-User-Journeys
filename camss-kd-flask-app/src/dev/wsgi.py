from main import app
import config.constants as constants

if __name__ == '__main__':
    app.run(port=constants.API_PORT, debug=constants.API_DEBUG)
