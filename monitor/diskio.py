from time import sleep
import psutil
from psutil._common import bytes2human
from monitor.config import DISK_INTERVAL

disk_read_speed_total = []
disk_write_speed_total = []
devices = psutil.disk_io_counters(perdisk=True).keys()
disk_read_speed_per = {device: [] for device in devices}
disk_write_speed_per = {device: [] for device in devices}


def _get_disk_io_speed():
    # not precise for unknown reasons
    disk_read_speed_total.append(psutil.disk_io_counters().read_bytes)
    disk_write_speed_total.append(psutil.disk_io_counters().write_bytes)
    for device in devices:
        disk_read_speed_per[device].append(
            psutil.disk_io_counters(perdisk=True)[device].read_bytes
        )
        disk_write_speed_per[device].append(
            psutil.disk_io_counters(perdisk=True)[device].write_bytes
        )
    sleep(DISK_INTERVAL)
    disk_read_speed_total.append(
        psutil.disk_io_counters().read_bytes - disk_read_speed_total[0]
    )
    disk_write_speed_total.append(
        psutil.disk_io_counters().write_bytes - disk_write_speed_total[0]
    )
    for device in devices:
        disk_read_speed_per[device].append(
            psutil.disk_io_counters(perdisk=True)[device].read_bytes
            - disk_read_speed_per[device][0]
        )
        disk_write_speed_per[device].append(
            psutil.disk_io_counters(perdisk=True)[device].write_bytes
            - disk_write_speed_per[device][0]
        )
    sleep(DISK_INTERVAL)
    while True:
        disk_read_speed_total.append(
            psutil.disk_io_counters().read_bytes
            - disk_read_speed_total[-1]
            - disk_read_speed_total[0]
        )
        disk_write_speed_total.append(
            psutil.disk_io_counters().write_bytes
            - disk_write_speed_total[-1]
            - disk_write_speed_total[0]
        )
        for device in devices:
            disk_read_speed_per[device].append(
                psutil.disk_io_counters(perdisk=True)[device].read_bytes
                - disk_read_speed_per[device][-1]
                - disk_read_speed_per[device][0]
            )
            disk_write_speed_per[device].append(
                psutil.disk_io_counters(perdisk=True)[device].write_bytes
                - disk_write_speed_per[device][-1]
                - disk_write_speed_per[device][0]
            )
        sleep(DISK_INTERVAL)


def get_disk_io_speed():
    return (
        [bytes2human(speed) for speed in disk_read_speed_total[1:]],
        [bytes2human(speed) for speed in disk_write_speed_total[1:]],
    )
