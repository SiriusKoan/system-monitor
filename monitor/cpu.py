from time import sleep
import psutil
from monitor.config import TIME_INTERVAL

cpu_usage_total = []
cpu_usage_per = []


def _get_cpu_usage():
    while True:
        cpu_usage_total.append(psutil.cpu_percent())
        cpu_usage_per.append(psutil.cpu_percent(percpu=True))
        sleep(TIME_INTERVAL)


def get_cpu_usage(per=False):
    return cpu_usage_per if per else cpu_usage_total

def clear_cpu():
    cpu_usage_total.clear()
    cpu_usage_per.clear()
