from api_views import Hello
from app import swagger_api


swagger_api.add_resource(Hello, "/hello")
