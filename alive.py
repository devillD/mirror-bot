from time import sleep
from requests import get as rget
from os import environ
from logging import error as logerror

BASE_URL = environ.get('BASE_URL_OF_BOT', None)
try:
    if len(BASE_URL) == 0:
        raise TypeError
    BASE_URL = BASE_URL.rstrip("/")
    PING_URL = "https://ping.up.railway.app/?link="
except TypeError:
    BASE_URL = None
PORT = environ.get('PORT', None)
if PORT is not None and BASE_URL is not None:
    while True:
        try:
            response = rget(f"{PING_URL}{BASE_URL}")
            print(response)
            sleep(600)
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
