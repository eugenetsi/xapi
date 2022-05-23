import json
import requests
from utils import *
from logger import setup_logger

logger = setup_logger('getters_logger', 'log.log')

def get_fixtures(headers, querystring, context):
  '''
  Gets fixtures according to context

  Parameters
  _________

          headers (dict): HOST/KEY
          querystring (dict): contains timezone info i.e \ 
            {"timezone":"Europe/Athens"}
          context (str): what fixtures are requested. 
            options: 'SL19' for 2019 Super League, 'LIVE' for live 

  Returns
  _______

          on success list of fixture dicts
          on failure []
  '''
  logger.info('{}'.format(context))
  if context == 'SL19':
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/787" # all fictures of 2019 super league
    response = requests.request("GET", url, headers=headers, params=querystring)
  elif context == 'LIVE':
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/live" # all live fictures
    response = requests.request("GET", url, headers=headers, params=querystring)
  else:
    logger.error('Incompatible input args: {},{}'.format(querystring, context))
    return []

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  data2 = data['api']
  data3 = data2['fixtures']
  #print_json(response.text)
  return data3

def get_odds(headers, fixture_id):
  '''
  Gets odds according to fixture_id from the bookmaker with
    the most events to bet on
  IMPORTANT: odds exist only 14 days before a match
    and are deleted 7 days after (possibly even before that)
 
  Call recommendation: 1/day

  Parameters
  _________

          headers (dict): HOST/KEY
          fixture_id (int): ex. 568052

  Returns
  _______

          on success list of dicts of kinds of bets and their odds
          on failure []
  '''
  logger.info('{}'.format(fixture_id))
  url = "https://rapidapi.p.rapidapi.com/v2/odds/fixture/" + str(fixture_id)
  response = requests.request("GET", url, headers=headers)
  #data = json.loads(response.text)
  try:
    data = json.loads(response.text) #get rid of init levels of json obj that are useless
    odds1 = data['api']
    odds2 = odds1['odds']
    if odds2 == []: # no odds exist
      logger.warning('no odds found for fixture {}, returning empty odds.'.format(fixture_id))
      return []
    '''
    max = 0
    index = 0
    for i in range(len(odds2[0]['bookmakers'])): # iterate through bookmakers
      current = len(odds2[0]['bookmakers'][i]['bets']) # and find the one with the max bets
      if current > max:
        max = current
        index = i

    res = odds2[0]['bookmakers'][index]['bets']
    res['fixture'] = odds2[0]['fixture']
    return res
    '''
    return odds2
  except Exception as e:
    logger.error('no odds found for fixture {}, returning empty odd. Error: {}'.format(fixture_id, e))
    return []

def get_predictions(headers, fixture_id):
  '''
  Gets predictions according to fixture_id
  Different from odds, this is algorithmic pred, using fish law, 
    comparison of team statistics, last matches, players etc.
  
  Call recommendation: 1/day

  Parameters
  _________

          headers (dict): HOST/KEY
          fixture_id (int): ex. 568052

  Returns
  _______

          on success list of dicts of predictions
          on failure []
  '''
  logger.info('{}'.format(fixture_id))
  if isinstance(fixture_id, int):
    url = "https://rapidapi.p.rapidapi.com/v2/predictions/" + str(fixture_id)
    response = requests.request("GET", url, headers=headers)
  else:
    return []
  
  data = json.loads(response.text) 
  preds = data['api']['predictions'] #get rid of init levels of json obj that are useless
  if preds == []: # no odds exist
    return []

  #print_json(response.text)
  return preds

def get_leagues(headers):
  '''
  Gets leagues

  Parameters
  _________

          headers (dict): HOST/KEY

  Returns
  _______

          on success list of league dicts
          on failure []
  '''
  logger.info('executing')
  url = "https://rapidapi.p.rapidapi.com/v2/leagues"
  response = requests.request("GET", url, headers=headers)

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  #print_json(response.text)
  leagues = data['api']['leagues']
  return leagues

def get_teams_from_league(headers, league_id):
  '''
  Gets teams from league id

  Parameters
  _________

          headers (dict): HOST/KEY
          league_id (int): unique id of league

  Returns
  _______

          on success list of team dicts
          on failure []
  '''
  logger.info('{}'.format(league_id))
  url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/" + str(league_id)
  response = requests.request("GET", url, headers=headers)

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  teams = data['api']['teams']
  return teams
  
def get_teams_from_id(headers, team_id):
  '''
  Gets teams from team id

  Parameters
  _________

          headers (dict): HOST/KEY
          team_id (int): unique id of league

  Returns
  _______

          on success list of team dicts
          on failure []
  '''
  logger.info('{}'.format(team_id))
  url = "https://api-football-v1.p.rapidapi.com/v2/teams/team/" + str(team_id)
  response = requests.request("GET", url, headers=headers)

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  teams = data['api']['teams']
  return teams

def get_fixtures_by_date(headers, querystring, date):
  '''
  Gets fixtures from specific date

  Parameters
  _________

          headers (dict): HOST/KEY
          querystring (dict): contains timezone info i.e
            {"timezone":"Europe/Athens"}
          context (str): the date of which to retrieve the fixtures from
            format: 'yyyy-mm-dd'

  Returns
  _______

          on success list of fixture dicts
          on failure []
  '''
  logger.info('{}'.format(date))
  if validate_date(date):
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/date/" + str(date)
    response = requests.request("GET", url, headers=headers, params=querystring)
  else:
    return []

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  return data['api']['fixtures']

def get_countries(headers):
  '''
  Gets countris from which we have availiable fixture data and
    their respective str codes

  Parameters
  _________

          headers (dict): HOST/KEY

  Returns
  _______

          on success list of country dicts
          on failure []
  '''

  logger.info('executing')
  url = "https://api-football-v1.p.rapidapi.com/v2/countries"
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  if data['api']['countries']:
    return data['api']['countries']
  else:
    return []

def get_seasons(headers):
  '''
  Gets seasons from which we have availiable fixture data

  Parameters
  _________

          headers (dict): HOST/KEY

  Returns
  _______

          on success list of season years
          on failure []
  '''

  logger.info('executing')
  url = "https://api-football-v1.p.rapidapi.com/v2/seasons"
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  if data['api']['seasons']:
    return data['api']['seasons']
  else:
    return []

def get_statistis_for_team(headers, league_id, team_id):
  '''
  Gets statistics for a specific team in a specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          league_id (int): unique id of league
          team_id (int): unique id of league

  Returns
  _______

          on success list of statistics dicts
          on failure []
  '''

  logger.info('{}, {}'.format(league_id, team_id))
  url = "https://api-football-v1.p.rapidapi.com/v2/statistics/" + str(league_id) + '/' + str(team_id)
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
  if data['api']['statistics']:
    return data['api']['statistics']
  else:
    return []

def get_statistis_for_fixture(headers, fixture_id):
  '''
  Gets statistics for a fixture

  Parameters
  _________

          headers (dict): HOST/KEY
          fixture_id (int): unique id of fixture

  Returns
  _______

          on success list of statistics dicts
          on failure []
  '''

  logger.info('{}'.format(fixture_id))
  url = "https://api-football-v1.p.rapidapi.com/v2/statistics/fixture/" + str(fixture_id)
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
  if data['api']['statistics']:
    return data['api']['statistics']
  else:
    return []

def get_fixtures_by_league(headers, querystring, league_id):
  '''
  Gets fixtures from specific league

  Parameters
  _________

          headers (dict)    : HOST/KEY
          querystring (dict): contains timezone info i.e
            {"timezone":"Europe/Athens"}
          league_id (int)   : league ID (PKey class League)

  Returns
  _______

          on success list of fixture dicts
          on failure []
  '''
  logger.info('{}'.format(league_id))
  url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/" + str(league_id)
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)

  if data['api']['fixtures']:
    return data['api']['fixtures']
  else:
    return []
