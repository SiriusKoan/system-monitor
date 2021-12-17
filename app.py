from threading import Thread
from blueprints import create_app
from monitor import cpu, diskio, memory, networkio, sysinfo, utils

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
timestamp_thread = Thread(target=utils.add_timestamp, daemon=True)
timestamp_thread.start()

app = create_app()
