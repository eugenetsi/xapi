import datetime
import os
import pickle
from Fixture import Fixture
from Odd import Odd
from getters import get_fixtures_by_date, get_odds
from utils import check_leagues, save_object, restore_object
from kafka import KafkaProducer
from logger import setup_logger

DEBUG = True

logger = setup_logger('actor_logger', 'log.log')

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'log.log')

HOST = os.environ.get("EXT_API_HOST_FOOTBALL")
KEY = os.environ.get("EXT_API_KEY_FOOTBALL")

querystring = {"timezone":"Europe/Athens"}

headers = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEY 
    }

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

logger.info("""                
    )          (    (     
 ( /(   (      )\ ) )\ )  
 )\())  )\    (()/((()/(  
((_)\((((_)(   /(_))/(_)) 
__((_))\ _ )\ (_)) (_))   
\ \/ /(_)_\(_)| _ \|_ _|  
 >  <  / _ \  |  _/ | |   
/_/\_\/_/ \_\ |_|  |___|  
                          """)
logger.info("***************************")

if DEBUG == True:
    logger.info('DEBUG mode selected')
    logger.info('Restoring Fixtures and Odds from saved pkls')
    Fixtures = restore_object('temp_fixtures.pkl')
    Odds = restore_object('temp_odds.pkl')

else:
    logger.info('Getting data for {}'.format(tomorrow))

    fixtures_raw = get_fixtures_by_date(headers, querystring, str(tomorrow))
    Fixtures = []

    # iterating through all fixtures from that day
    # selecting those belonging to the approved leagues
    # and creating the Fixtures object list
    for fraw in fixtures_raw:
        if check_leagues(fraw['league_id']):
            Fixtures.append(Fixture(**fraw))

    #save_object(Fixtures, 'temp_fixtures.pkl')
    logger.info("Got {} Fixtures from day {}".format(len(Fixtures), tomorrow))

    odds_raw = []
    Odds = []
    for f in Fixtures:
        temp_odd = get_odds(headers, f.fixture_id)
        if temp_odd:
            odds_raw.append(temp_odd)

    for odd in odds_raw:
        Odds.append(Odd(**odd[0]))
    #save_object(Odds, 'temp_odds.pkl')


logger.info("Got {} Fixtures and {} odds from day {}".format(len(Fixtures), len(Odds), tomorrow))

logger.info('Starting kafka producer')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: pickle.dumps(x))

for f in Fixtures:
    producer.send('fixtures', value=f)
    logger.info("sending Fixture {}".format(f.fixture_id))

for odd in Odds:
    producer.send('odds', value=odd)
    logger.info("sending odds for Fixture {}".format(odd.fixture_id))

producer.flush()
producer.close()
