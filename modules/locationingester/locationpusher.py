import json
import os, sys
import logging
from kafka import KafkaConsumer
from sqlalchemy import create_engine

TOPIC_NAME = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_CONSUMER_URL = os.environ["KAFKA_CONSUMER_URL"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_CONSUMER_URL])

# Function to generate handlers for logging
def create_logging_handlers():
    # set logger to handle STDOUT and STDERR
    stdout_handler =  logging.StreamHandler(stream=sys.stdout) # stdout handler `
    stderr_handler =  logging.StreamHandler(stream=sys.stderr) # stderr handler
    file_handler = logging.FileHandler(filename='locationingester.log')
    handlers = [stderr_handler, stdout_handler, file_handler]
    return handlers

def write_to_database(location):
    engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    conn = engine.connect()
    person_id = int(location["userId"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])
    insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(person_id, latitude, longitude)

    logging.info(insert)
    conn.execute(insert)

format_output = '%(levelname)s:%(name)s:%(asctime)s, %(message)s'
logging.basicConfig(format=format_output, level=logging.INFO, handlers=create_logging_handlers())
logging.info("locationingester is consuming topic {} from {}.".format(KAFKA_TOPIC, KAFKA_CONSUMER_URL))
url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(user=DB_USERNAME, passwd=DB_PASSWORD, host=DB_HOST, port=DB_PORT, db=DB_NAME)
logging.info("locationingester is consuming topic {} from {}.".format(KAFKA_TOPIC, KAFKA_CONSUMER_URL))


for location in consumer:
    message = location.value.decode('utf-8')
    print('{}'.format(message))
    location_message = json.loads(message)
    write_to_database(location_message)
