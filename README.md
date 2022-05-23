# External API (xapi)

************************** **CAUTION** **************************

>max api calls per day: 100, after that we get charged

>max api calls per minute: 30

>response time ~ 150ms

>DO NOT upload api key - host only on local machine

>Do not write over the pickled data

************************** **CAUTION** **************************

## Table of Contents
1. [Usage](#usage)
2. [Pipeline](#pipeline)
3. [Scheduling](#scheduling)
4. [Football](#football)
    1. [Classes](#classes-f)
    2. [Functionality](#functionality-f)
    3. [Getters](#getters-f)
    4. [Utilities](#utilities-f)
    5. [Pickled Data](#pickled_data-f)
5. [Basketball](#basketball)
    1. [Classes](#classes-b)
    2. [Functionality](#functionality-b)
    3. [Getters](#getters-b)
    4. [Utilities](#utilities-b)
    5. [Pickled Data](#pickled_data-b)
6. [Logging](#logging)
7. [Disclaimer](#disclaimer)



## Usage <a name="usage"></a>
To use the external API you have to create environment variables
with the names `EXT_API_HOST_FOOTBALL` and `EXT_API_KEY_FOOTBALL`,
export the variables and source the script. Ask me to get the working keys.

Example script is provided in `./example_ext_api`.

Edit the host/key pair and remove the word `example_` from 
the filename so it gets ignored by `.gitignore`.

> NEVER EVER UPLOAD `./ext_api` LIKE SERIOUSLY PINKY SWEAR 

```lang-bash
>>> cp example_ext_api ext_api && source ext_api
```

To install the package requirements that are needed to run /xapi run the following:
```lang-bash
pip install -r requirements.txt 
```

## Pipeline <a name="pipeline"></a>
The execution path is: 
- the Scheduler `scheduler.py` creates a chronjob of defined frequency. To that chronjob it assigns the Actor.
- The Actor `actor.py` brings the data over, cleans them, creates classes etc, and calls the KafkaProducer.
- The KafkaProducer `kafka_producer.py` opens a stream and encodes the data appropriately and sends them over to KafkaConsumer.
- The KafkaConsumer `kafka_consumer.py` spins up threads (this can also be changed for multiprocessing), digests the data sent over the stream with the defined group IDs, decodes them and gets them ready for database insertion.

## Scheduling <a name="scheduling"></a>
The module gets fixtures and their odds for the next day, once per day. This will change.

# Football <a name="football"></a>

## Classes <a name="classes-f"></a>

Last letter in the name denotes the sport, in this case F is for Football (right now this is not implemented in football, because it breaks everything and I don't want to touch it, but it is implemented in basketball).

- Stucture.py
	- `Structure` // General purpose base class.
- Fixture.py
	- `Fixture` // Container for matches' info. PKey: fixture_id, FKey: league_id (League), FKey: homeTeam-awayTeam (Team).
- League.py
	- `League` // Container for leagues. PKey: league_id.
- Team.py
	- `Team` // Container for teams. PKey: team_id.
- Odd.py
	- `Odd` // Container for odds. FKey: fixture_id.

## Functionality <a name="functionality-f"></a>
- can show all leagues in country in year
- can show all live fixtures
- can show all fixtures in league
- can show all odds for given fixture
- can show all predictions for given fixture
- can show all leagues
- can show all teams in league
- can show all fixtures from one date
- can show all countries
- can show all seasons
- can show all statistics for one team
- can show all statistics for one fixture
- can show all fixtures from specific league

## Getters <a name="getters-f"></a>
- `get_fixtures()` returns list of dicts of fixtures
- `get_odds()` returns bets and their odds for fixture
- `get_predictions()` returns algorithmic predictions for fixture
- `get_leagues()` returns all leagues
- `get_teams_from_id()` returns team that has that specific id
- `get_teams_from_league()` returns teams from that specific league
- `get_fixtures_by_date()` returns fixtures from a specific date
- `get_countries()` returns countries that we have availiable data for
- `get_seasons()` returns seasons that we have availiable data for
- `get_statistics_for_team()` returns statistics for a specific team in a specific league
- `get_statistics_for_fixture()` returns statistics for fixture
- `get_fixtures_by_league()` returns fixtures from specific league

## Utilities <a name="utilities-f"></a>
- `print_json()` print json objects in readable form
- `save_object()` saves pickle of object
- `restore_object()` returns the pickle
- `validate_date()` type datetime checks
- `check_leagues()` checks whether a league_id exists in the approved league list
- `unix_to_human()` datetime conversion from unix to human readble
- `find_league()` finds league based on ID
- `find_team()` finds team based on ID

## Pickled Data <a name="pickled_data-f"></a>
This is temporary storage, not to be used in production. Now, it is used as a middle ground between the xAPI and the DB.
- `Fixtures.pkl` contains list of FixtureF objects
- `Leagues.pkl` contains list of LeagueF objects
- `Teams.pkl` contains list of TeamF objects

# Basketball <a name="basketball"></a>

## Classes <a name="classes-b"></a>

Last letter in the name denotes the sport, in this case B is for Basketball.

- StuctureB.py
	- `StructureB` // General purpose base class.
- GameB.py
	- `GameB` // Container for games' info. PKey: game_id, FKey: league_id (LeagueB), FKey: awayTeam-homeTeam (TeamB).

## Functionality <a name="functionality-b"></a>
- can show all games from one date
- can show all head-to-head games between 2 teams
- can show all teams from a season in a league
- can show all statistics about a team in a season/league
- can show all standings from a season in a league
- can show all groups from a season in a league
- can show all stages from a season in a league
- can show all leagues
- can show all seasons

## Getters <a name="getters-b"></a>
- `get_games_by_date()` returns list of games from date
- `get_games_h2h()` returns list of head-to-head games between 2 teams
- `get_teams_by_season_league()` returns list of teams from the season and league
- `get_teams_by_season_league()` returns list of team statistics by season/league/team id
- `get_standings_by_season_league()` returns list of standings from the season and league
- `get_groups_by_season_league()` returns list of groups from the season and league
- `get_stages_by_season_league()` returns list of stages from the season and league
- `get_leagues()` returns dict of leagues
- `get_seasons()` returns list of seasons

## Utilities <a name="utilities-b"></a>
- `print_json()` print json objects in readable form
- `validate_date()` type datetime checks

## Pickled Data <a name="pickled_data-b"></a>

# Logging <a name="logging"></a>
| Level      | When it is used |
| ----------- | ----------- |
| DEBUG      | Detailed information, typically of interest only when diagnosing problems.|
| INFO      | Confirmation that things are working as expected.|
| WARNING      | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.|
| ERROR   | Due to a more serious problem, the software has not been able to perform some function.|
| CRITICAL      | A serious error, indicating that the program itself may be unable to continue running.|

# Disclaimer <a name="disclaimer"></a>
"A few things I am not. I am not a cat. I am not an institutional investor, nor am I a hedge fund. I do not have clients and I do not provide personalized investment advice for fees or commissions." -DFV
