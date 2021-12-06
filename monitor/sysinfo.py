import psutil


def get_cpu_count():
    return psutil.cpu_count()


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


def get_battery_info():
    battery = psutil.sensors_battery()
    return {
        "percent": battery.percent,
        "secsleft": battery.secsleft,
        "power_plugged": battery.power_plugged,
    }
