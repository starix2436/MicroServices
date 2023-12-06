from concurrent import futures
import grpc
import grpc_config.auth_pb2
import grpc_config.auth_pb2_grpc
from loggers import logger


class AuthServer(grpc_config.auth_pb2_grpc.NotificationsServicer):
    def GetUserDetails(self, request, context):
        logger.info("GetUserDetails request was made.")
        print(request.id)
        detail_reply = grpc_config.auth_pb2.UserDetailResponse()
        detail_reply.first_name = "Nihal"
        # request.first_name
        return detail_reply


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_config.auth_pb2_grpc.add_NotificationsServicer_to_server(AuthServer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
