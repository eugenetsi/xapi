import requests
import json
import os
from Fixture import Fixture
from League import League
from Team import Team
from Odd import Odd
from utils import *
from getters import *
import time
from logger import setup_logger
from kafka import KafkaProducer

"""
***************** CAUTION **************************
max api calls per day: 100, after that we get charged
response time ~ 300ms
DO NOT upload api key - host only on local machine
***************** CAUTION **************************

To use the external api you have to create environment variables
with the names <EXT_API_HOST> and <EXT_API_KEY>,
export the variables and source the script.
Example script is provided in ./example_ext_api.
Edit the host/key pair and remove the word example_ from 
the filename so it gets ignored by .gitignore.

"""

"""
Logging Levels:

Level       When it’s used
_____       ______________

DEBUG       Detailed information, typically of interest only when 
            diagnosing problems.

INFO        Confirmation that things are working as expected.

WARNING     An indication that something unexpected happened, or indicative 
            of some problem in the near future (e.g. ‘disk space low’). 
            The software is still working as expected.

ERROR       Due to a more serious problem, the software has not been able 
            to perform some function.

CRITICAL    A serious error, indicating that the program itself may be unable 
            to continue running.
"""

'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(module)s:%(name)s:%(funcName)s: %(message)s', datefmt='%Y:%m:%d::%H:%M:%S')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#logging.basicConfig(level=logging.DEBUG, 
#                    format='%(levelname)s:%(asctime)s:%(name)s: %(message)s')
'''

logger = setup_logger('global_logger', 'log.log')

HOST = os.environ.get("EXT_API_HOST_FOOTBALL")
KEY = os.environ.get("EXT_API_KEY_FOOTBALL")

querystring = {"timezone":"Europe/Athens"}

headers = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEY 
    }

Fixtures = restore_object('Fixtures.pkl')
Leagues = restore_object('Leagues.pkl')
Teams = restore_object('Teams.pkl')

# USE SCHEDULE OR CHRONTAB

'''
#################################################################
# run this part only once for init, if pickle files do not exist, 
or to update them
#################################################################

fixtures_raw = get_fixtures(headers, querystring, 'SL19')
Fixtures = []
for f in range(len(fixtures_raw)):
    Fixtures.append(Fixture(**fixtures_raw[f]))

save_object(Fixtures, 'Fixtures.pkl')

#temp = fixtures_list[0].fixture_id
#print(f"id of random fixture: {temp}") 
# printing the first games' id from the FixtureF obj list
#print(get_odds(headers, temp))

#print(get_predictions(headers, 635612))
#print(get_leagues(headers))


leagues_raw = get_leagues(headers)
Leagues = []
for l in range(len(leagues_raw)):
  Leagues.append(League(**leagues_raw[l]))

save_object(Leagues, 'Leagues.pkl')

#print(f'first league id: {Leagues[0].league_id}')

Teams = []
tid = []
teams_raw = get_teams_from_league(headers, 1)
for t in range(len(teams_raw)):
  Teams.append(Team(**teams_raw[t]))
  tid.append(Teams[t].team_id)

print(tid)
save_object(Teams, 'Teams.pkl')
#################################################################
'''

'''

#teams_raw = get_teams_from_league(headers, 1)
#print(teams_raw[0]['team_id'])

tid = []
for t in range(len(Teams)):
    tid.append(Teams[t].team_id)
    #print(Teams[t].name)

logger.info("Team IDs: {}".format(len(tid)))

for t in range(len(Leagues)):
    print("League ID {}, Name: {}, Season_start: {}".format(Leagues[t].league_id, Leagues[t].name, Leagues[t].season_start))
'''

'''
lid = []
for l in range(len(Leagues)):
    lid.append(Leagues[l].league_id)
    print(Leagues[l].league_id)

print("League IDs: ", len(lid))
'''

'''
for i in range(3000, 3027):
    print('League: ', i)
    teams_raw = get_teams_from_league(headers, i)
    time.sleep(3)
    for t in range(len(teams_raw)): 
        if teams_raw[t]['team_id'] in tid:
            continue
        else:
            Teams.append(Team(**teams_raw[t]))
            tid.append(teams_raw[t]['team_id'])
            print("Team IDs: ", len(tid))

save_object(Teams, 'Teams.pkl')
'''

'''
#teams_raw = get_teams_from_league(headers, 1)
Teams = []
tid = []

for t in range(len(teams_raw)):
  Teams.append(Team(**teams_raw[t]))
  tid.append(Teams[t].team_id)

print(tid)
save_object(Teams, 'Teams.pkl')
'''

'''
Fixtures = []
for id in [524, 565, 775]:
  fixtures_raw = get_fixtures_by_league(headers, querystring, id)
  for f in range(len(fixtures_raw)):
    Fixtures.append(Fixture(**fixtures_raw[f]))
    print("Adding FIxture ID:", Fixtures[f].fixture_id)

save_object(Fixtures, 'Fixtures_that_George_requested.pkl')
'''

'''
for iter in range(len(Leagues)):
    if Leagues[iter].league_id == 2905:
        print(Leagues[iter])
'''

'''
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

fixtures_raw = get_fixtures_by_date(headers, querystring, str(today))
Fixtures = []
for f in range(len(fixtures_raw)):
    Fixtures.append(Fixture(**fixtures_raw[f]))

k = 0
for f in Fixtures:
  for l in Leagues:
    if f.league_id == l.league_id:
      if l.season == 2020:
        print(f, l)
        for t in Teams:
            if t.team_id == f.homeTeam:
                print(t)
            if t.team_id == f.awayTeam:
                print(t)
'''

'''
import re

logger.info('\n')
for l in Leagues:
    #if l.country == "Netherlands" and l.season == 2020 or l.season == 2021:
    if re.search("Bundesliga", l.name, re.IGNORECASE) and (l.season == 2020 or l.season == 2021):
    #if re.search("primera", l.name, re.IGNORECASE) and l.country == 'Spain':
    #if l.country == 'Spain':
        #logger.info(f'\n{l.name}: {l.league_id}, {l.season}, {l.country}')
        print(l)
'''

'''
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

fixtures_raw = get_fixtures_by_date(headers, querystring, str(tomorrow))
Fixtures = []
for fraw in fixtures_raw:
    if check_leagues(fraw['league_id']):
        Fixtures.append(Fixture(**fraw))

odds_raw = []
Odds = []
for f in Fixtures:
    odds_raw.append(get_odds(headers, f.fixture_id))

for odd in odds_raw:
    Odds.append(Odd(**odd[0]))

print(f'Tomorrow on {tomorrow}:')
for f in Fixtures:
    team1 = find_team(f.homeTeam, Teams).name
    team2 = find_team(f.awayTeam, Teams).name
    lname = find_league(f.league_id, Leagues).name

    print(f'In league {lname}:')
    print(f'{team1} is playing against {team2}')
    print(f'on {f.venue}')
    print('with odds:')
    print(f'From {Odds[0].bookmaker_name}:')
    print(f'for example {Odds[0].bets[0]["label_name"]} with bets: {Odds[0].bets[0]["values"]}')
    print(f'other types of bets on the match also availiable:')
    approved_bets = ['Asian Handicap', 'Goals Over/Under',
                 'HT/FT Double', 'Both Teams Score', 'Exact Score',
                 'Double Chance', 'First Half Winner', 'Team To Score First',
                 'Both Teams Score - First Half', 'To Win Either Half',
                 'Results/Both Teams Score', 'Result/Total Goals']
    print(approved_bets)
'''

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

logger.info("Got {} Fixtures".format(len(Fixtures)))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         api_version=(0,11,5),
                         value_serializer=lambda x: pickle.dumps(x))

for f in Fixtures:
    producer.send('fixtures', value=f)
    logger.info("sending Fixture {}".format(f.fixture_id))

