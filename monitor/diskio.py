from time import sleep
import psutil
from monitor.config import TIME_INTERVAL

disk_read_speed_total = []
disk_write_speed_total = []
devices = psutil.disk_io_counters(perdisk=True).keys()
# disk_read_speed_per = {device: [] for device in devices}
# disk_write_speed_per = {device: [] for device in devices}


def _get_disk_io_speed():
    disk_read_speed_total.append(psutil.disk_io_counters().read_bytes)
    disk_write_speed_total.append(psutil.disk_io_counters().write_bytes)
    # for device in devices:
    #     disk_read_speed_per[device].append(
    #         psutil.disk_io_counters(perdisk=True)[device].read_bytes
    #     )
    #     disk_write_speed_per[device].append(
    #         psutil.disk_io_counters(perdisk=True)[device].write_bytes
    #     )
    while True:
        disk_read_speed_total.append(
            psutil.disk_io_counters().read_bytes - disk_read_speed_total[0]
        )
        disk_write_speed_total.append(
            psutil.disk_io_counters().write_bytes - disk_write_speed_total[0]
        )
        # for device in devices:
        #     disk_read_speed_per[device].append(
        #         psutil.disk_io_counters(perdisk=True)[device].read_bytes
        #         - disk_read_speed_per[device][0]
        #     )
        #     disk_write_speed_per[device].append(
        #         psutil.disk_io_counters(perdisk=True)[device].write_bytes
        #         - disk_write_speed_per[device][0]
        #     )
        sleep(TIME_INTERVAL)


def get_disk_io_speed(per=False):
    read = [disk_read_speed_total[1]]
    read += [
        disk_read_speed_total[index] - disk_read_speed_total[index - 1]
        for index in range(2, len(disk_read_speed_total))
    ]
    write = [disk_write_speed_total[1]]
    write += [
        disk_write_speed_total[index] - disk_write_speed_total[index - 1]
        for index in range(2, len(disk_write_speed_total))
    ]
    # read_per = {device: [disk_read_speed_per[device][1]] for device in devices}
    # write_per = {device: [disk_write_speed_per[device][1]] for device in devices}
    # for device in devices:
    #     read_per[device] += [
    #         disk_read_speed_per[device][index] - disk_read_speed_per[device][index - 1]
    #         for index in range(2, len(disk_read_speed_per[device]))
    #     ]
    #     write_per[device] += [
    #         disk_write_speed_per[device][index]
    #         - disk_write_speed_per[device][index - 1]
    #         for index in range(2, len(disk_write_speed_per[device]))
    #     ]
    # if per:
        # return read_per, write_per
    return read, write

def clear_disk_io_speed():
    read_total_tmp = disk_read_speed_total[-1]
    write_total_tmp = disk_write_speed_total[-1]
    disk_read_speed_total.clear()
    disk_write_speed_total.clear()
    disk_read_speed_total.append(read_total_tmp)
    disk_write_speed_total.append(write_total_tmp)
    # for device in devices:
    #     read_per_tmp = disk_read_speed_per[device][-1]
    #     write_per_tmp = disk_write_speed_per[device][-1]
    #     disk_read_speed_per[device].clear()
    #     disk_write_speed_per[device].clear()
    #     disk_read_speed_per[device].append(read_per_tmp)
    #     disk_write_speed_per[device].append(write_per_tmp)
