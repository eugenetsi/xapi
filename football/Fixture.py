from Structure import Structure

class Fixture(Structure):
    '''
    Class for FixturesF i.e. football games between two TeamsF.

    Attributes
    __________

        awayTeam (int): FKey class TeamF
        elapsed (int):
        event_date (str):
        event_timestamp (int):
        firstHalfStart (int):
        fixture_id (int): 
        goalsAwayTeam (int):
        goalsHomeTeam (int):
        homeTeam (int): FKey class TeamF
        league_id (int): FKey class LeagueF
        referee (str):
        round (str):
        score (dict):
        secondHalfStart (int):
        status (str):
        statusShort (str):
        venue (str):

    Methods
    _______

        __eq__(obj): compares equality based on fixture_id
        __str__(obj): prints some attributes of the object
        fly_banner(): flies banner
    '''

    _fields = [('awayTeam', int), ('elapsed', int), ('event_date', str),
               ('event_timestamp', int), ('firstHalfStart', int),
               ('fixture_id', int), ('goalsAwayTeam', int), ('goalsHomeTeam', int),
               ('homeTeam', int), ('league_id', int),
               ('referee', str), ('round', str), ('score', dict),
               ('secondHalfStart', int), ('status', str), ('statusShort', str),
               ('venue', str)]

    def __init__(self, *args, **kwargs):
        if 'events' in kwargs:
            del kwargs['events']
        if 'league' in kwargs:
            del kwargs['league'] # don't need league info just the id, since we have all the leagues with more info stored
        kwargs['awayTeam'] = kwargs['awayTeam']['team_id'] # same for teams
        kwargs['homeTeam'] = kwargs['homeTeam']['team_id']
        super(Fixture, self).__init__(*args, **kwargs)

    def __eq__(self, other):
      return self.fixture_id == other.fixture_id

    def __str__(self):
        return f'fixture_id: {self.fixture_id}\n league_id: {self.league_id}\n awayTeam: {self.awayTeam}\n homeTeam: {self.homeTeam}\n event_date: {self.event_date}\n venue: {self.venue}\n'


    def fly_banner(self):
        print('flying banner')
