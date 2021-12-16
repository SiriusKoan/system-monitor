from threading import Thread
from monitor import cpu, diskio, memory, networkio, sysinfo
from utils import add_timestamp, timestamps

cpu_thread = Thread(target=cpu._get_cpu_usage, daemon=True)
cpu_thread.start()
mem_thread = Thread(target=memory._get_vir_memory_usage, daemon=True)
mem_thread.start()
diskio_thread = Thread(target=diskio._get_disk_io_speed, daemon=True)
diskio_thread.start()
networkio_thread = Thread(target=networkio._get_network_io_speed, daemon=True)
networkio_thread.start()
battery_thread = Thread(target=sysinfo._get_battery_info, daemon=True)
battery_thread.start()
timestamp_thread = Thread(target=add_timestamp, daemon=True)
timestamp_thread.start()


while True:
    command = input("Enter command: ")
    if command == "cpu_usage":
        print(cpu.get_cpu_usage())
    elif command == "vir_mem_usage":
        print(memory.get_vir_memory_usage())
    elif command == "vir_mem_usage_percent":
        print(memory.get_vir_memory_usage_percent())
    elif command == "swap_mem_usage":
        print(memory.get_swap_memory_usage())
    elif command == "swap_mem_usage_percent":
        print(memory.get_swap_memory_usage_percent())
    elif command == "cpu_count":
        print(sysinfo.get_cpu_count())
    elif command == "boot_time":
        print(sysinfo.get_boot_time())
    elif command == "disk_usage":
        print(sysinfo.get_disk_usage())
    elif command == "battery_info":
        print(sysinfo.get_battery_info())
    elif command == "disk_io":
        print(diskio.get_disk_io_speed())
    elif command == "network_io":
        print(networkio.get_network_io_speed())
    elif command == "timestamps":
        print(timestamps, len(timestamps))
    elif command == "uptime":
        print(sysinfo.get_boot_time())
    elif command == "exit":
        print("Exiting...")
        break
    else:
        print("Command not found")
