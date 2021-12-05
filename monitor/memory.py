from time import sleep
import psutil
from psutil._common import bytes2human
from monitor.config import MEMORY_INTERVAL


# virtual memory
vir_memory_usage = []


def get_vir_total_memory():
    return bytes2human(psutil.virtual_memory().total)


def _get_vir_memory_usage():
    while True:
        mem = psutil.virtual_memory()
        vir_memory_usage.append(
            {
                "available": bytes2human(mem.available),
                "used": bytes2human(mem.used),
                "percent": mem.percent,
            }
        )
        sleep(MEMORY_INTERVAL)


def get_vir_memory_usage():
    return vir_memory_usage

def get_vir_memory_usage_percent():
    return psutil.virtual_memory().percent


# swap memory
swap_memory_usage = []


def get_swap_total_memory():
    return bytes2human(psutil.swap_memory().total)


def _get_swap_memory_usage():
    while True:
        mem = psutil.swap_memory()
        swap_memory_usage.append(
            {
                "free": bytes2human(mem.free),
                "used": bytes2human(mem.used),
                "percent": mem.percent,
            }
        )
        sleep(MEMORY_INTERVAL)


def get_swap_memory_usage():
    return swap_memory_usage

def get_swap_memory_usage_percent():
    return psutil.swap_memory().percent