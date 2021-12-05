from threading import Thread
from monitor import cpu, memory

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
    elif command == "exit":
        break