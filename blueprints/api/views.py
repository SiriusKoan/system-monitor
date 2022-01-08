from flask import jsonify
from monitor import cpu, diskio, memory, networkio, sysinfo, utils
from . import api_bp


@api_bp.route("/api/cpu_usage")
def cpu_usage_api():
    response = jsonify(
        {
            "cpu_usage_total": cpu.get_cpu_usage(),
            "cpu_usage_per": cpu.get_cpu_usage(per=True),
        }
    )
    return response


@api_bp.route("/api/memory_usage")
def memory_usage_api():
    response = jsonify(
        {
            "vir_memory_usage": memory.get_vir_memory_usage(),
            "vir_memory_usage_percent": memory.get_vir_memory_usage_percent(),
            "swap_memory_usage": memory.get_swap_memory_usage(),
            "swap_memory_usage_percent": memory.get_swap_memory_usage_percent(),
        }
    )
    return response


@api_bp.route("/api/disk_io")
def disk_io_api():
    data = diskio.get_disk_io_speed()
    data_per = diskio.get_disk_io_speed(per=True)
    print(data_per)
    response = jsonify(
        {
            "disk_io_speed_total": {"read": data[0], "write": data[1]},
            "disk_io_speed_per": {"read": data_per[0], "write": data_per[1]},
        }
    )
    return response


@api_bp.route("/api/network_io")
def network_io_api():
    data = networkio.get_network_io_speed()
    data_per = networkio.get_network_io_speed(per=True)
    response = jsonify(
        {
            "network_io_speed_total": {"input": data[0], "output": data[1]},
            "network_io_speed_per": {"input": data_per[0], "output": data_per[1]},
        }
    )
    return response


@api_bp.route("/api/sysinfo")
def sysinfo_api():
    response = jsonify(
        {
            "battery_info": sysinfo.get_battery_info(),
            "cpu_count": sysinfo.get_cpu_count(),
            "vir_total_memory": sysinfo.get_vir_total_memory(),
            "swap_total_memory": sysinfo.get_swap_total_memory(),
            "boot_time": sysinfo.get_boot_time(),
            "disk_usage": sysinfo.get_disk_usage(),
            "disks_partitions": sysinfo.get_disks_partitions(),
        }
    )
    return response


@api_bp.route("/api/timestamp")
def timestamp_api():
    response = jsonify(
        {
            "timestamp": utils.get_timestamp(),
        }
    )
    return response
