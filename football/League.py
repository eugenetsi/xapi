from Structure import Structure

class League(Structure):
    '''
    Class for LeaguesF. There are ~3000 leagues.

    Attributes
    __________

        league_id (int): PKey
        name (str):
        type (str):
        country (str):
        country_code (str):
        season (int):
        season_start (str):
        season_end (str):
        logo (str): link of the league logo
        flag (str):
        standings (int):
        is_current (int):

    Methods
    _______

        __eq__(obj): compares equality based on league_id
        __str__(obj): prints some attributes of the object
        fly_banner(): flies banner
    '''

    _fields = [('league_id', int), ('name', str), ('type', str), ('country', str), 
               ('country_code', str), ('season', int), ('season_start', str), 
               ('season_end', str), ('logo', str), ('flag', str), 
               ('standings', int), ('is_current', int)]

    def __init__(self, *args, **kwargs):
        if 'coverage' in kwargs:
            del kwargs['coverage']
        super(League, self).__init__(*args, **kwargs)

    def __eq__(self, other):
        return self.league_id == other.league_id

    def __str__(self):
        return f'league_id: {self.league_id}\n name: {self.name}\n country: {self.country}\n season: {self.season}\n'

    def fly_banner(self):
        print('flying banner')
