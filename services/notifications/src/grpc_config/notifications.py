import grpc
import auth_pb2
import auth_pb2_grpc
import time

# client

# def get_client_stream_requests():
#     while True:
#         email = input("Please enter a name (or nothing to stop chatting): ")

#         if email == "":
#             break
#         detail_request = grpc_config.auth_pb2.UserDetailRequest(id=6)
#         yield detail_request
#         time.sleep(1)


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = auth_pb2_grpc.NotificationsStub(channel)
        detail_request = auth_pb2.UserDetailRequest(id=8)
        detail_reply = stub.GetUserDetails(detail_request)
        print(detail_reply)


if __name__ == "__main__":
    run()


# def run():
#     # Connect to the gRPC server
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = auth_pb2_grpc.NotificationsStub(channel)

#         # Create a user request with an ID
#         userreq = auth_pb2.UserDetailRequest(id=6)

#         # Make a gRPC call to the server and receive the response
#         userres = stub.GetUserDetails(userreq)

#         # Process the received user details
#         print(userres.first_name, userres.last_name, userres.email)


# if __name__ == "__main__":
#     run()
