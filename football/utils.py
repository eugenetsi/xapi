import requests
import json
import pickle
import datetime
from datetime import datetime as dt
from datetime import timezone
from logger import setup_logger

logger = setup_logger('utils_logger', 'log.log')

def print_json(resp):
  semi_parsed = json.loads(resp)
  parsed = json.dumps(semi_parsed, indent=4, sort_keys=True)
  print(parsed)


def save_object(obj, filename):
  '''
  Pickles obj to filename.
    if filename exists, it overwrites it

  Parameters
  _________

          obj (whetever): the object you want to pickle
          filename (str): the filename you want to save to

  Returns
  _______

          nothing
  '''
  with open(filename, 'wb') as output:  # Overwrites any existing file.
    logger.info('{}'.format(filename))
    pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def restore_object(filename):
  '''
  Restores pickled file to object.

  Parameters
  _________

          filename (str): the filename of the pickle you want to restore

  Returns
  _______

          the object contained in the pickle
  '''
  with open(filename, 'rb') as input:
    obj = pickle.load(input)
    logger.info('{}'.format(filename))
    return obj

def validate_date(date_text):
    # validates whether date is in correct format

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def check_leagues(id):
  '''
  Checks whether a league id exists in the approved league list.
  
  Approved Leagues: [Premier League (eng),  Championship(eng),  LaLiga(esp), 
  Bundesliga (ger), Serie A (ita), Ligue 1 (fra), Primeira Liga (por), 
  Super League (gre), Eredivise (hol), Champions League (eur), 
  Europa League (eur), Euro (national), Allsvenskan (swe), Eliteserien (nor), 
  Superliga (dan), Premier League (rus), Super Lig (tur), LaLiga 2 (esp), 
  Bundesliga 2 (ger), Ligue 2 (fra), Serie B (ita), Super League 2(gre), 
  Super League (swi), Tipico Bundesliga (aus)]

  Parameters
  _________

          id (int)   : league ID (PKey class League)

  Returns
  _______

          True/False depending on whether the id is valid 
  '''

  #approved = [2790, 2794, 2833, 2755, 2857, 2664, 2826, 2874, 2673, 2771, 2777, 403, 1329, 1310, 2705, 2679, 2816, 2847, 2743, 2652, 2946, 2980, 2855, 2779]

  #approved = [3886, 3501, 3513, 3510, 3576, 3506, 3575, 3676, 3437, 1422, 3632, 3490, 3176, 3307, 3428, 3459, 3552, 3516, 3509, 3511, 3630, 3938, 3175, 3508]

  approved = [3886, 3501, 3513, 3510, 3576, 3506, 3575, 3676, 3437, 1422, 3632, 3490]

  if id in approved:
    return True
  else:
    return False

def unix_to_human(utime):
    '''
    Converts unix time to datetime, assuming time is in seconds
    if in miliseconds divide by 100.

    Parameters
    _________

          utime (int)   : Unix timestamp

    Returns
    _______

          Datetime string %Y-%m-%d %H:%M:%S
    '''

    x = dt.fromtimestamp(utime, tz=timezone.utc)
    return x.strftime('%Y-%m-%d %H:%M:%S')

def find_league(league_id, Leagues):
    '''
    Finds league based on id.

    Parameters
    _________

          league_id (int)   : league ID (PKey class League)

    Returns
    _______

          League obj
    '''

    for league in Leagues:
        if league.league_id == league_id:
            return league
    logger.warning("league ID not found in Leagues")

def find_team(team_id, Teams):
    '''
    Finds team based on id.

    Parameters
    _________

          team_id (int)   : team ID (PKey class Team)

    Returns
    _______

          Team obj
    '''

    for team in Teams:
        if team.team_id == team_id:
            return team
    logger.warning("team ID not found in Teams")
