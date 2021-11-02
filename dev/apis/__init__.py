from flask_restx import Api
from apis.camss_assessments import api as ca

api = Api(title='CAMSS solutions Microservices', version='0.1',
          description="CAMSS solutions microservices documentation and testing.")

api.add_namespace(ca)
