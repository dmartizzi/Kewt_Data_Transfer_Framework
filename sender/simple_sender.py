import json
import random
from time import sleep

import requests


def post_random_numbers(url,n):
    session = requests.Session()
    session.trust_env = False
    for _ in range(n):
        a = random.random()
        b = random.random()
        msg = json.dumps({"body" : {"a": a, "b": b}})
        session.post(url, data=msg)
        sleep(1)

if __name__ == "__main__":
    url = "http://listener:8000/post_data_to_db"
    sleep(30)
    post_random_numbers(url,1000)
