import grpc
import auth_pb2
import auth_pb2_grpc
from models import User


class GetUser(auth_pb2_grpc.NotificationsServicer):
    def GetUserDetails(self, request, context):
        user = User.query.filter_by().all()
        return user
