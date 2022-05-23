from Structure import Structure
from getters import unix_to_human
from logger import setup_logger

logger = setup_logger('odd_logger', 'log.log')

class Odd(Structure):
    '''
    Class for odds of fixtures.
    See local variable for approved types of bets.
    Heavy preference to Bet365.

    Attributes
    __________

        fixture_id (int)    : FKey class Fixture
        league_id (int)     : FKey class League
        bets (dict)         : dictionary of type of bet and odd
        bookmaker_id (int)  : unique id of bookmaker
        bookmaker_name (str): name of the bookmaker
        updated_at (int)    : Unix time

    Methods
    _______

        __eq__(obj)         : compares equality based on fixture_id and league_id
        __str__(obj)        : printing handler
        adjust_odds(offset) : adusting all availiable odds by a multiplier (offset)
                            to account for the houses' edge and make odds fair
        fly_banner()        : flies banner
        '''

    _fields = [('fixture_id', int), ('league_id', int), ('bets', list),
               ('bookmaker_id', int), ('bookmaker_name', str),
               ('updated_at', int)]


    def __init__(self, *args, **kwargs):
        self.approved_bets = ['Match Winner', 'Asian Handicap', 'Goals Over/Under',
                     'HT/FT Double', 'Both Teams Score', 'Exact Score',
                     'Double Chance', 'First Half Winner', 'Team To Score First',
                     'Both Teams Score - First Half', 'To Win Either Half',
                     'Results/Both Teams Score', 'Result/Total Goals']

        kwargs['fixture_id'] = kwargs['fixture']['fixture_id']
        kwargs['league_id'] = kwargs['fixture']['league_id']
        kwargs['updated_at'] = kwargs['fixture']['updateAt']
        del kwargs['fixture']
        kwargs['bookmaker_id'] = -1
        kwargs['bets'] = []
        for bmaker in range(len(kwargs['bookmakers'])):
            if kwargs['bookmakers'][bmaker]['bookmaker_name'] == 'Bet365':
                kwargs['bookmaker_id'] = kwargs['bookmakers'][bmaker]['bookmaker_id']
                kwargs['bookmaker_name'] = kwargs['bookmakers'][bmaker]['bookmaker_name']
                for bet in kwargs['bookmakers'][bmaker]['bets']:
                    if bet['label_name'] in self.approved_bets:
                        kwargs['bets'].append(bet)

        # if Bet365 is not found select 0-th
        if kwargs['bookmaker_id'] == -1:
            logger.warning('Bet365 not found in bookmakers; selecting 0th - this might cause problems down the line.')
            #print('Bet365 not found in bookmakers; selecting 0th - this might cause problems down the line.')
            kwargs['bookmaker_id'] = kwargs['bookmakers'][0]['bookmaker_id']
            kwargs['bookmaker_name'] = kwargs['bookmakers'][0]['bookmaker_name']
            for bet in kwargs['bookmakers'][0]['bets']:
                if bet['label_name'] in approved_bets:
                    kwargs['bets'].append(bet)

        del kwargs['bookmakers']
        super(Odd, self).__init__(*args, **kwargs)

    def adjust_odds(self, offset=1.052):
        for bet in self.bets:
            for item in bet['values']:
                newval = float("{:.2f}".format(float(item['odd']) * 1.052))
                item['odd'] = newval

    def __eq__(self, other):
        return (self.fixture_id == other.fixture_id) and (self.league_id == other.league_id)

    def __str__(self):
        return f' fixture_id: {self.fixture_id}\n league_id: {self.league_id}\n bookmaker_name: {self.bookmaker_name}\n updated_at: {unix_to_human(self.updated_at)}\n'

    def fly_banner(self):
        print('flying banner')
