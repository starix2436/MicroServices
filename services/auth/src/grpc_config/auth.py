import grpc
from grpc_config import auth_pb2
from grpc_config import auth_pb2_grpc


class GetUser(auth_pb2_grpc.NotificationsServicer):
    def GetUserDetails(self, request, context):
        # Assuming a notification service is available at localhost:50051
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = auth_pb2_grpc.NotificationsStub(channel)

            # Making a gRPC call to the notification service to get user details
            userreq = auth_pb2.UserDetailRequest(id=request.id)
            userres = stub.GetUserDetails(userreq)
            print(userres)
            # Return the received user details back to the client
            return userres
