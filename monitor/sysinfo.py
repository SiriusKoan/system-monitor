from time import sleep
import psutil
from psutil._common import bytes2human
from monitor.config import BATTERY_INTERVAL
from utils import add_timestamp

battery_usage = []


def get_cpu_count():
    return psutil.cpu_count()


def get_vir_total_memory():
    return bytes2human(psutil.virtual_memory().total)


def get_swap_total_memory():
    return bytes2human(psutil.swap_memory().total)


def get_boot_time():
    return psutil.boot_time()


def get_disk_usage():
    disks = [disk.device for disk in psutil.disk_partitions()]
    return [
        {
            "device": disk,
            "total": psutil.disk_usage(disk).total,
            "used": psutil.disk_usage(disk).used,
            "free": psutil.disk_usage(disk).free,
            "percent": psutil.disk_usage(disk).percent,
        }
        for disk in disks
    ]


def _get_battery_info():
    while True:
        battery = psutil.sensors_battery()
        battery_usage.append(
            {
                "percent": battery.percent,
                "power_plugged": battery.power_plugged,
            }
        )
        sleep(BATTERY_INTERVAL)


def get_battery_info():
    return battery_usage
