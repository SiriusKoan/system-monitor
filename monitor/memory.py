from time import sleep
import psutil
from psutil._common import bytes2human
from monitor.config import TIME_INTERVAL


# virtual memory
vir_memory_usage = []


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
        sleep(TIME_INTERVAL)


def get_vir_memory_usage():
    return vir_memory_usage


def get_vir_memory_usage_percent():
    return [usage["percent"] for usage in vir_memory_usage]


# swap memory
swap_memory_usage = []


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
        sleep(TIME_INTERVAL)


def get_swap_memory_usage():
    return swap_memory_usage


def get_swap_memory_usage_percent():
    return [usage["percent"] for usage in swap_memory_usage]


def clear_memory():
    vir_memory_usage.clear()
    swap_memory_usage.clear()
