from app import swagger_api
from .api_views import Hello, SignUp, Login, UserDetails, UserList, UpdateUser, DeleteUser

swagger_api.add_resource(Hello, "/hello")
swagger_api.add_resource(SignUp, "/signup")
swagger_api.add_resource(Login, "/login")
swagger_api.add_resource(UserDetails, "/details")
swagger_api.add_resource(UserList, "/userlist")
swagger_api.add_resource(UpdateUser, "/update")
swagger_api.add_resource(DeleteUser, "/delete")
