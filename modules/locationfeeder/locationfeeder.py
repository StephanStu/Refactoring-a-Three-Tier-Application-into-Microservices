from flask import Flask, request
import os, logging, sys, json
from kafka import KafkaProducer

# Function to generate handlers for logging
def create_logging_handlers():
    # set logger to handle STDOUT and STDERR
    stdout_handler =  logging.StreamHandler(stream=sys.stdout) # stdout handler `
    stderr_handler =  logging.StreamHandler(stream=sys.stderr) # stderr handler
    file_handler = logging.FileHandler(filename='locationfeeder.log')
    handlers = [stderr_handler, stdout_handler, file_handler]
    return handlers

app = Flask(__name__)
# Route for posting requests and getting a default request
@app.route("/", methods=['GET', 'POST'])
def post_location():
    global producer
    if request.method == 'POST':
        payload = request.json
        userId = payload['userId']
        if userId < 0:
            logging.error("userId must be larger than zero!")
            return {"status": "not-ok"}, 422
        else:
            latitude = payload['latitude']
            longitude = payload['longitude']
            request_payload = {
                'userId': userId,
                'latitude': latitude,
                'longitude': longitude
            }
            logging.info("processing request with payload " + json.dumps(request_payload))
            encoded_data = json.dumps(request_payload, indent=2).encode('utf-8')
            try:
                producer.send(topic, encoded_data)
                logging.info("post-request received, user #{} is located at {}, {}".format(userId, latitude, longitude))
                return {"status": "ok"}, 200
            except:
                logging.error("failed to push payload into the message queue.")
                return {"status": "not-ok"}, 500
    else:
        logging.info("post-endpoint called by GET-Method, returning an example json-formatted request.")
        return {"userId": 000, "latitude": 000, "longitude": 000}, 200

# start the application on port 5001
if __name__ == "__main__":
    # Initialize the logging
    format_output = '%(levelname)s:%(name)s:%(asctime)s, %(message)s'
    logging.basicConfig(format=format_output, level=logging.DEBUG, handlers=create_logging_handlers())
    logging.info("locationposter is listening on port 5001.")
    try:
        broker = os.environ["KAFKA_PRODUCER_URL"]
        logging.info("connecting to broker at " + broker)
        topic = os.environ["KAFKA_TOPIC"]
        logging.info("using the topic " + topic)
        producer = KafkaProducer(bootstrap_servers=broker)
    except:
        logging.error("unable to connect to Kafka.")
    # Starts the application on host:port
    app.run(host='0.0.0.0', port='5001')
