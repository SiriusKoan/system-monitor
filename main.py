from threading import Thread
from monitor import cpu, memory, sysinfo

cpu_thread = Thread(target=cpu._get_cpu_usage, daemon=True)
cpu_thread.start()
mem_thread = Thread(target=memory._get_vir_memory_usage, daemon=True)
mem_thread.start()

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
    elif command == "exit":
        break