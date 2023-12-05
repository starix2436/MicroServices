import grpc
from concurrent import futures
from grpc_config.auth_pb2_grpc import add_NotificationsServicer_to_server
from grpc_config.auth import GetUser


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_NotificationsServicer_to_server(GetUser(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
