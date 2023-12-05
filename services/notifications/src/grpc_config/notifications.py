import grpc
import auth_pb2
import auth_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = auth_pb2_grpc.NotificationsStub(channel)
        userreq = auth_pb2.UserDetailRequest(id=6)
        print(userreq, "##############")
        userres = stub.GetUserDetails(userreq)
        print(userres, "##############")


if __name__ == "__main__":
    run()
