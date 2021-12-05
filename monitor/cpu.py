from time import sleep
import psutil

from monitor.config import CPU_INTERVAL

cpu_usage_total = []
cpu_usage_per = []


def get_cpu_count():
    return psutil.cpu_count()


def _get_cpu_usage():
    while True:
        cpu_usage_total.append(psutil.cpu_percent())
        cpu_usage_per.append(psutil.cpu_percent(percpu=True))
        sleep(CPU_INTERVAL)


def get_cpu_usage(percpu=False):
    return cpu_usage_per if percpu else cpu_usage_total
