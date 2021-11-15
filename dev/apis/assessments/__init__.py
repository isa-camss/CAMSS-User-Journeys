from flask_restx import Api
from apis.assessments.camss_assessments import api as ca

api = Api(title='CAMSS solutions Microservices',
          description="CAMSS solutions microservices documentation and testing.")

api.add_namespace(ca)
