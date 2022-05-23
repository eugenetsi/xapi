from utils import *

def get_games_by_date(headers, date):
  '''
  Gets fixtures from specific date 

  Parameters
  _________

          headers (dict): HOST/KEY
          date (str): the date of which to retrieve the fixtures from
            format: 'yyyy-mm-dd'

  Returns
  _______

          on success list of game dicts
          on failure []
  '''
  if validate_date(date):
    querystring = {"date": date}
    url = "https://api-basketball.p.rapidapi.com/games"
    response = requests.request("GET", url, headers=headers, params=querystring)
  else:
    return []

  data = json.loads(response.text) #get rid of init levels of json obj that are useless
  return data['response']

def get_teams_by_season_league(headers, season, league):
  '''
  Gets fixtures from specific season from specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          season (str): the date season of the games
            format: 'yyyy-yyyy'
          league (int): the league that the games belong
            format: int

  Returns
  _______

          on success list of team dicts
          on failure []
  '''

  querystring = {"league": str(league), "season": season}
  url = "https://api-basketball.p.rapidapi.com/teams"
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    return []

def get_standings_by_season_league(headers, season, league):
  '''
  Gets standings from specific season from specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          season (str): the date season of the games
            format: 'yyyy-yyyy'
          league (int): the league that the games belong
            format: int

  Returns
  _______

          on success list of season dicts
          on failure []
  '''

  querystring = {"league": str(league), "season": season}
  url = "https://api-basketball.p.rapidapi.com/standings"
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    print(data['errors'])
    return []

def get_groups_by_season_league(headers, season, league):
  '''
  Gets groups from specific season from specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          season (str): the date season of the games
            format: 'yyyy-yyyy'
          league (int): the league that the games belong
            format: int

  Returns
  _______

          on success list of groups
          on failure []
  '''

  querystring = {"league": str(league), "season": season}
  url = "https://api-basketball.p.rapidapi.com/standings/groups"
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    print(data['errors'])
    return []

def get_stages_by_season_league(headers, season, league):
  '''
  Gets stages from specific season from specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          season (str): the date season of the games
            format: 'yyyy-yyyy'
          league (int): the league that the games belong
            format: int

  Returns
  _______

          on success list of stages
          on failure []
  '''

  querystring = {"league": str(league), "season": season}
  url = "https://api-basketball.p.rapidapi.com/standings/stages"
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    print(data['errors'])
    return []

def get_leagues(headers):
  '''
  Gets leagues

  Parameters
  _________

          headers (dict): HOST/KEY

  Returns
  _______

          on success dict of leagues
          on failure []
  '''

  url = "https://api-basketball.p.rapidapi.com/leagues"
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    raise Exception(data['errors'])
    return []

def get_games_h2h(headers, team1, team2):
  '''
  Gets head2head games from two teams

  Parameters
  _________

          headers (dict): HOST/KEY
          team1 (int): first team ID
          team2 (int): second team ID

  Returns
  _______

          on success list of game dicts
          on failure []
  '''
  h2h = str(team1) + '-' + str(team2)
  querystring = {"h2h": h2h}
  url = "https://api-basketball.p.rapidapi.com/games"
  response = requests.request("GET", url, headers=headers, params=querystring)

  data = json.loads(response.text)
  return data['response']

def get_seasons(headers):
  '''
  Gets seasons

  Parameters
  _________

          headers (dict): HOST/KEY

  Returns
  _______

          on success list of seasons
          on failure []
  '''

  url = "https://api-basketball.p.rapidapi.com/seasons"
  response = requests.request("GET", url, headers=headers)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    raise Exception(data['errors'])
    return []

def get_team_stats(headers, season, league, team_id):
  '''
  Gets satistics about a team with team_id
    from specific season from specific league

  Parameters
  _________

          headers (dict): HOST/KEY
          season (str): the date season of the games
            format: 'yyyy-yyyy'
          league (int): the league that the games belong
            format: int
          team_id (int): PKey of team

  Returns
  _______

          on success list of team dicts
          on failure []
  '''

  querystring = {"league": str(league), "season": season, "team": str(team_id)}
  url = "https://api-basketball.p.rapidapi.com/statistics"
  response = requests.request("GET", url, headers=headers, params=querystring)
  data = json.loads(response.text)
  if data['response']:
    return data['response']
  else:
    raise Exception(data['errors'])
    return []
