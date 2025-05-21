import grpc
import greet_pb2
import greet_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = greet_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(greet_pb2.HelloRequest(name='World'))
print("Response:", response.message)
