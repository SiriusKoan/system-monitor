from datetime import datetime
from time import sleep
from monitor.config import TIME_INTERVAL

timestamps = []


def add_timestamp():
    while True:
        timestamp = int(datetime.timestamp(datetime.now()))
        timestamps.append(timestamp)
        sleep(TIME_INTERVAL)


def get_timestamp():
    return timestamps

def clear_timestamp():
    timestamps.clear()
