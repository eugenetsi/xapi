from kafka import KafkaProducer
from Fixture import Fixture
from time import sleep
from json import dumps
from utils import restore_object
import pickle
from logger import setup_logger

logger = setup_logger('kafka_producer_logger', 'log.log')

Fixtures = restore_object('Fixtures.pkl')
Leagues = restore_object('Leagues.pkl')
Teams = restore_object('Teams.pkl')

'''
NOTE: switch to avro as the serializer/deserializer format
    for efficiency
    https://www.confluent.io/blog/avro-kafka-data/
'''

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: pickle.dumps(x))
                         #value_serializer=lambda x: dumps(x))
                         #value_serializer=lambda x:
                         #dumps(x).encode('utf-8'))

for f in Fixtures:
    producer.send('fixtures', value=f)
    logger.info("sending Fixture {}".format(f.fixture_id))
    #sleep(1.5)

for l in Leagues:
    producer.send('leagues', value=l)
    logger.info("sending League {}".format(l.league_id))
    #sleep(1.5)

for t in Teams:
    producer.send('teams', value=t)
    logger.info("sending Team {}".format(t.team_id))
    #sleep(1.5)

'''
# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'First_Topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers = bootstrap_servers, api_version=(0,11,5))

# Publish text in defined topic
producer.send(topicName, b'Hello from kafka...')

# Print message
print("Message Sent")
'''
