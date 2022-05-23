from kafka import KafkaConsumer
from Fixture import Fixture
from time import sleep
from json import loads
import pickle
import threading
from logger import setup_logger

logger = setup_logger('kafka_consumer_logger', 'log.log')

# CONSUMER DEFINITIONS

Fconsumer = KafkaConsumer(
    'fixtures',
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='VSB_f_f',
    value_deserializer=lambda x: pickle.loads(x))

Lconsumer = KafkaConsumer(
    'leagues',
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='VSB_f_l',
    value_deserializer=lambda x: pickle.loads(x))

Tconsumer = KafkaConsumer(
    'teams',
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='VSB_f_t',
    value_deserializer=lambda x: pickle.loads(x))

Oconsumer = KafkaConsumer(
    'odds',
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='VSB_f_o',
    value_deserializer=lambda x: pickle.loads(x))

# CONSUMER FUNCTIONS

def consume_fixtures(Fconsumer):
    for msg in Fconsumer:
        val = msg.value
        logger.info("recieved Fixture: {}".format(val.fixture_id))
        ########
        # here do actions on data
        ########

def consume_leagues(Lconsumer):
    for msg in Lconsumer:
        val = msg.value
        logger.info("recieved League: {}".format(val.league_id))
        ########
        # here do actions on data
        ########

def consume_teams(Tconsumer):
    for msg in Tconsumer:
        val = msg.value
        logger.info("recieved Team: {}".format(val.team_id))
        ########
        # here do actions on data
        ########

def consume_odds(Oconsumer):
    for msg in Oconsumer:
        val = msg.value
        logger.info("recieved odds for Fixture: {}".format(val.fixture_id))
        ########
        # here do actions on data
        ########

# assigning threads to consumers
thrF = threading.Thread(target=consume_fixtures, args=(Fconsumer, ))
#thrL = threading.Thread(target=consume_leagues, args=(Lconsumer, ))
#thrT = threading.Thread(target=consume_teams, args=(Tconsumer, ))
thrO = threading.Thread(target=consume_odds, args=(Oconsumer, ))

# starting individual threads
thrF.start()
#thrL.start()
#thrT.start()
thrO.start()
