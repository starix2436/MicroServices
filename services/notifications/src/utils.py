import grpc
import grpc_config.auth_pb2
import grpc_config.auth_pb2_grpc


from models import EmailNotification
from app import db


# remove run fucntion use inside code in different fucntion call it add user store its data in db there
# create another fucntion aah make class and the define fucntions inside that and do email send
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = grpc_config.auth_pb2_grpc.NotificationsStub(channel)
        detail_request = grpc_config.auth_pb2.UserDetailRequest(id=3)
        detail_reply = stub.GetUserDetails(detail_request)
        print(detail_reply)
        print(detail_reply.first_name)

        user_data = EmailNotification(
            first_name=detail_reply.first_name,
            last_name=detail_reply.last_name,
            email=detail_reply.email,
        )
        db.session.add(user_data)
        db.session.commit

        # store_data(detail_reply)


if __name__ == "__main__":
    run()
