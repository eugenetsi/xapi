import requests
import json
import pickle
import os
import time
import datetime

def print_json(resp):
  semi_parsed = json.loads(resp)
  parsed = json.dumps(semi_parsed, indent=4, sort_keys=True)
  print(parsed)

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
