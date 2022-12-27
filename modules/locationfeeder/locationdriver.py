import grpc
import location_pb2
import location_pb2_grpc

# This script simulates injection of location data as expected from a mobile
# application connecting to our service.

print("Coordinates sending...")

# Works with the deployed VM
channel = grpc.insecure_channel("127.0.0.1:30011")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
user1_location = location_pb2.Location(
    userId=300,
    latitude=-100,
    longitude=30
)

user2_location = location_pb2.Location(
    userId=400,
    latitude=-100,
    longitude=30
)

response_1 = stub.Create(user1_location)
response_2 = stub.Create(user2_location)


print("Coordinates sent...")
print(response_1)
print(response_2)
