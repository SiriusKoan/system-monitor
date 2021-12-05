from threading import Thread
from monitor import cpu

cpu_thread = Thread(target=cpu.get_cpu_percent, daemon=True)
cpu_thread.start()

while True:
    command = input("Enter command: ")
    if command == "cpu_usage":
        print(cpu.get_cpu_usage())
