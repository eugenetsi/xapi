from kafka import KafkaConsumer
from Fixture import Fixture
from time import sleep
from json import loads
import pickle
import threading
from logger import setup_logger

logger = setup_logger('kafka_consumer_logger', 'log.log')

# CONSUMER DEFINITIONS

Consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0,11,5),
    #auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=None,
    #group_id='VSB_f',
    value_deserializer=lambda x: pickle.loads(x))

# CONSUMER FUNCTIONS

def consume_fixtures(msg):
    val = msg.value
    logger.info("recieved Fixture: {}".format(val.fixture_id))
    ########
    # here do actions on data
    ########

def consume_leagues(msg):
    val = msg.value
    logger.info("recieved League: {}".format(val.league_id))
    ########
    # here do actions on data
    ########

def consume_teams(msg):
    val = msg.value
    logger.info("recieved Team: {}".format(val.team_id))
    ########
    # here do actions on data
    ########

def consume_odds(msg):
    val = msg.value
    logger.info("recieved Odd: {}".format(val.fixture_id))
    ########
    # here do actions on data
    ########

# assigning topics to consumers
Consumer.subscribe(topics=('fixtures', 'odds'))

func_dict = {"fixtures": consume_fixtures,
             "odds": consume_odds,
             "leagues": consume_leagues,
             "teams": consume_teams}

for msg in Consumer:
    func_dict[msg.topic](msg)
