import requests
import json
from utils import *
from getters import *
import time

HOST = os.environ.get("EXT_API_HOST_BASKETBALL")
KEY = os.environ.get("EXT_API_KEY_BASKETBALL")

querystring = {"timezone":"Europe/Athens"}

headers = {
    'x-rapidapi-host': HOST,
    'x-rapidapi-key': KEY
    }

print(get_games_by_date(headers, '2019-01-01'))
