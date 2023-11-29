from app import swagger_api
from .api_views import Hello

swagger_api.add_resource(Hello, "/hello")
