import grpc
import location_pb2
import location_pb2_grpc
import os, logging, sys, json
from concurrent import futures
from kafka import KafkaProducer

broker = os.environ["KAFKA_URL"]
logging.info("connecting to broker at " + broker)
topic = os.environ["KAFKA_TOPIC"]
logging.info("using the topic " + topic)
producer = KafkaProducer(bootstrap_servers=broker)

def create_logging_handlers():
    # set logger to handle STDOUT and STDERR
    stdout_handler =  logging.StreamHandler(stream=sys.stdout) # stdout handler `
    #stderr_handler =  logging.StreamHandler(stream=sys.stderr) # stderr handler
    file_handler = logging.FileHandler(filename='locationfeeder.log')
    handlers = [stdout_handler, file_handler]
    return handlers

class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def Create(self, request, context):
        request_payload = {
            'userId': int(request.userId),
            'latitude': int(request.latitude),
            'longitude': int(request.longitude)
        }
        logging.info("processing request with payload " + json.dumps(request_payload))
        encoded_data = json.dumps(request_payload, indent=2).encode('utf-8')
        try:
            producer.send(topic, encoded_data)
        except:
            logging.error("failed to push payload into the message queue.")

        return location_pb2.Location(**request_payload)

format_output = '%(levelname)s:%(name)s:%(asctime)s, %(message)s'
logging.basicConfig(format=format_output, level=logging.DEBUG, handlers=create_logging_handlers())
server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
logging.info('locationfeeder is listening on port 5001')
server.add_insecure_port('[::]:5001')
server.start()
server.wait_for_termination()
