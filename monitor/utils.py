from datetime import datetime
from time import sleep

timestamps = []

def add_timestamp():
    while True:
        timestamp = int(datetime.timestamp(datetime.now()))
        timestamps.append(timestamp)
        sleep(1)
