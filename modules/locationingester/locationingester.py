from kafka import KafkaConsumer
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
import os, sys, json, logging

KAFKA_CONSUMER_URL = os.environ["KAFKA_CONSUMER_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

# Get SQLalchemy engine using credentials.
def get_database(url):
    if not database_exists(url):
        logging.error("database does not exist or database is not reachable from locationingester.")

    database = create_engine(url, pool_size=50, echo=True)
    return database

# Function to generate handlers for logging
def create_logging_handlers():
    # set logger to handle STDOUT and STDERR
    stdout_handler =  logging.StreamHandler(stream=sys.stdout) # stdout handler `
    stderr_handler =  logging.StreamHandler(stream=sys.stderr) # stderr handler
    file_handler = logging.FileHandler(filename='locationingester.log')
    handlers = [stderr_handler, stdout_handler, file_handler]
    return handlers

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_CONSUMER_URL])
format_output = '%(levelname)s:%(name)s:%(asctime)s, %(message)s'
logging.basicConfig(format=format_output, level=logging.INFO, handlers=create_logging_handlers())
logging.info("locationingester is consuming topic {} from {}.".format(KAFKA_TOPIC, KAFKA_CONSUMER_URL))
url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(user=DB_USERNAME, passwd=DB_PASSWORD, host=DB_HOST, port=DB_PORT, db=DB_NAME)
try:
    database = get_database(url)
    database_is_available = True
    logging.info("connected successfully to database")
except:
    database_is_available = False
    logging.error("did not connect to database")

for location in consumer:
    logging.info("received {}".format(location.value.decode('utf-8')))
    print(location.value.decode('utf-8'))
    if database_is_available:
        print("accessing database")
        with database.connect() as connection:
            payload = json.loads(location.value.decode('utf-8'))
            userId = payload["userId"]
            latitude = payload["latitude"]
            longitude = payload["longitude"]
            # inpsired by https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
            #insert_statement = "INSERT INTO location (userId, coordinate) VALUES ({}, ST_Point({}, {}))".format(userId, latitude, longitude)
            #connection.execute(insert_statement)
