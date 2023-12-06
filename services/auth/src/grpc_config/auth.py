import grpc
from grpc_config import auth_pb2
from grpc_config import auth_pb2_grpc
from loggers import logger
# from auth_pb2_grpc import UserM
# class GetUser(auth_pb2_grpc.NotificationsServicer):
#     def GetUserDetails(self, request, context):
#         # Assuming a notification service is available at localhost:50051
#         with grpc.insecure_channel("localhost:50051") as channel:
#             stub = auth_pb2_grpc.NotificationsStub(channel)

#             # Making a gRPC call to the notification service to get user details
#             userreq = auth_pb2.UserDetailRequest(id=request.id)
#             userres = stub.GetUserDetails(userreq)
#             print(userres)
#             # Return the received user details back to the client
#             return userres

class AuthServer(auth_pb2_grpc.NotificationsServicer):
    def GetUserDetails(self, request, context):
        from utils import UserManager

        logger.info("GetUserDetails request was made.")
        print(request.id)
        
        user_data = UserManager().details(id=request.id)
        print(user_data)
        detail_reply = auth_pb2.UserDetailResponse()
        #detail_reply.first_name = "Nihal"
        detail_reply.first_name = "user_data.first_name"

        # request.first_name
        return detail_reply