import grpc
import auth_pb2
import auth_pb2_grpc


def run():
    # Connect to the gRPC server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = auth_pb2_grpc.NotificationsStub(channel)

        # Create a user request with an ID
        userreq = auth_pb2.UserDetailRequest(id=6)

        # Make a gRPC call to the server and receive the response
        userres = stub.GetUserDetails(userreq)

        # Process the received user details
        print(userres.first_name, userres.last_name, userres.email)


if __name__ == "__main__":
    run()
