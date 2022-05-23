from Structure import Structure

class Team(Structure):
    '''
    Class for TeamsF

    Attributes
    __________

        team_id (int): PKey
        name (str):
        code (str):
        logo (str):
        country (str):
        is_national (bool):
        founded (int): 
        venue_name (str):
        venue_surface (str):
        venue_address (str):
        venue_city (str):
        venue_capacity (int):

    Methods
    _______

        __eq__(obj): compares equality based on fixture_id
        __str__(obj): prints some attributes of the object
        fly_banner(): flies banner
    '''

    _fields = [('team_id', int), ('name', str), ('code', str), ('logo', str),
              ('country', str), ('is_national', bool), ('founded', int), 
              ('venue_name', str), ('venue_surface', str), ('venue_address', str),
              ('venue_city', str), ('venue_capacity', int)]

    def __init__(self, *args, **kwargs):
        super(Team, self).__init__(*args, **kwargs)

    def __eq__(self, other):
      return self.team_id == other.team_id

    def __str__(self):
        return f'team_id: {self.team_id}\n name: {self.name}\n country: {self.country}\n venue_city: {self.venue_city}\n venue_name: {self.venue_name}\n'

    def fly_banner(self):
        print('flying banner')
