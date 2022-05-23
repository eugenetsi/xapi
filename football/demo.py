from Fixture import Fixture
from League import League
from Team import Team
from utils import *

Fixtures = restore_object('Fixtures.pkl')
Leagues = restore_object('Leagues.pkl')
Teams = restore_object('Teams.pkl')


print("Fixtures: ", len(Fixtures))
print("Leagues: ", len(Leagues))
print("Teams: ", len(Teams))

print('Fixture obj example (not all attr):\n', Fixtures[0])
