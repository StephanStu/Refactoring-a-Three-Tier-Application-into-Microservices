from kafka import KafkaConsumer
from sqlalchemy import create_engine
import os, json

KAFKA_URL = os.environ["KAFKA_CONSUMER_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

# Function to generate handlers for logging
def create_logging_handlers():
    # set logger to handle STDOUT and STDERR
    stdout_handler =  logging.StreamHandler(stream=sys.stdout) # stdout handler `
    stderr_handler =  logging.StreamHandler(stream=sys.stderr) # stderr handler
    file_handler = logging.FileHandler(filename='locationfeeder.log')
    handlers = [stderr_handler, stdout_handler, file_handler]
    return handlers

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL])
format_output = '%(levelname)s:%(name)s:%(asctime)s, %(message)s'
logging.basicConfig(format=format_output, level=logging.DEBUG, handlers=create_logging_handlers())
logging.info("locationingester is consuming topic {} from {}.".format(KAFKA_TOPIC,KAFKA_CONSUMER_URL))

for location in consumer:
    logging.info("received {}".format(location.value.decode('utf-8')))
