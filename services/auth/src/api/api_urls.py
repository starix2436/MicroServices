from app import swagger_api
from .api_views import Hello, SignUp, Login

swagger_api.add_resource(Hello, "/hello")
swagger_api.add_resource(SignUp, "/signup")
swagger_api.add_resource(Login, "/login")
