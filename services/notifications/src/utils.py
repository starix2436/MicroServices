# import grpc
# import grpc_config.auth_pb2
# # from grpc_config import auth_pb2
# # from grpc_config import auth_pb2_grpc

# import grpc_config.auth_pb2_grpc
# #import time
# from models import EmailNotification
# from app import db 
# # client

# # def get_client_stream_requests():
# #     while True:
# #         email = input("Please enter a name (or nothing to stop chatting): ")

# #         if email == "":
# #             break
# #         detail_request = grpc_config.auth_pb2.UserDetailRequest(id=6)
# #         yield detail_request
# #         time.sleep(1)

# # def store_data(detail_reply):

# #     #client_data = EmailNotification(detail_reply)

# #     print(detail_reply)
# #     # db.session.add(client_data)
# #     # db.session.commit()
    
# def run():
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = grpc_config.auth_pb2_grpc.NotificationsStub(channel)
#         detail_request = grpc_config..UserDetailRequest(id=3)
#         detail_reply = stub.GetUserDetails(detail_request)
#         print(detail_reply)
#         print(detail_reply.first_name)

#         user_data= EmailNotification(
#             first_name=detail_reply.first_name,
#             last_name=detail_reply.last_name,
#             email=detail_reply.email,

#         )
#         db.session.add(user_data)
#         db.session.commit

#         # store_data(detail_reply)




# if __name__ == "__main__":
#     run()


# # def run():
# #     # Connect to the gRPC server
# #     with grpc.insecure_channel("localhost:50051") as channel:
# #         stub = auth_pb2_grpc.NotificationsStub(channel)

# #         # Create a user request with an ID
# #         userreq = auth_pb2.UserDetailRequest(id=6)

# #         # Make a gRPC call to the server and receive the response
# #         userres = stub.GetUserDetails(userreq)

# #         # Process the received user details
# #         print(userres.first_name, userres.last_name, userres.email)


# # if __name__ == "__main__":
# #     run()
