import grpc
from gRPC.source import helloworld_pb2_grpc, helloworld_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='world'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()