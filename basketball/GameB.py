class GameB(StructureB):
    '''
    Class for basketball Games i.e. events between two teams.

    Attributes
    __________

        country_id (int) :  where the Game is played
        date (str)       :  when the game is played in <timezone>
        game_id (int)    :  PKey of Game
        league_id (int)  :  FKey of class LeagueB
        scores (dict)    :  dict with quarter scores of away/home teams
        stage (dict)     :  ?? don't know yet
        status (dict)    :  status of the game
        awayTeam (int)   :  FKeay of class TeamB
        homeTeam (int)   :  FKey of class TeamB
        time (str)       :  time in the game
        timestamp (int)  :  time in the game reflected to <timezone>
        timezone (str)   :  timezone the the times refer to
        week (str)       :  week name

    Methods
    _______

        __eq__(obj)     :   compares equality based on game_id
        __str__()       :   prints certain identifying attributes of self
                              mainly for debugging
        reshape_input   :   shortens input and changes keys such that they
                              reflect the glabal naming conventions
        fly_banner()    :   flies banner
    '''

    _fields = [('country_id', int), ('date', str), ('game_id', int),
               ('league_id', int), ('scores', dict),
               ('stage', dict), ('status', dict), ('awayTeam', int),
               ('homeTeam', int), ('time', str),
               ('timestamp', int), ('timezone', str), ('week', str)]

    def __init__(self, *args, **kwargs):
        kwargs = self.reshape_input(**kwargs)
        super(GameB, self).__init__(*args, **kwargs)
      
    def reshape_input(self, *args, **kwargs):
      result = {'country_id': kwargs['country']['id'],
                'date': kwargs['date'],
                'game_id': kwargs['id'],
                'league_id': kwargs['league']['id'],
                'scores': kwargs['scores'],
                'stage': kwargs['stage'],
                'status': kwargs['status'],
                'awayTeam': kwargs['teams']['away']['id'],
                'homeTeam': kwargs['teams']['home']['id'],
                'time': kwargs['time'],
                'timestamp': kwargs['timestamp'],
                'timezone': kwargs['timezone'],
                'week': kwargs['week']
                }
      return result

    def __eq__(self, other):
      return self.game_id == other.game_id

    def __str__(self):
        return (f' game_id: {self.game_id}\n league_id: {self.league_id}\n'
        f' awayTeam: {self.awayTeam}\n homeTeam: {self.homeTeam}\n'
        f' country_id: {self.country_id}\n week: {self.week}\n')

    def fly_banner(self):
        print('flying banner')
