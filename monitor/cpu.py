from time import sleep
import psutil

cpu_usage = []

def get_cpu_count():
    return psutil.cpu_count()


def get_cpu_percent():
    while True:
        cpu_usage.append(psutil.cpu_percent(percpu=True))
        sleep(1)

def get_cpu_usage():
    return cpu_usage
