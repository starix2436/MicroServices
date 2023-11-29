from app import swagger_api
from .api_views import Hello, sign_up, Login

swagger_api.add_resource(Hello, "/hello")
swagger_api.add_resource(sign_up, "/signup")
swagger_api.add_resource(Login, "/login")
