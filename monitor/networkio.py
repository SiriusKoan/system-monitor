from time import sleep
import psutil
from monitor.config import NETWORK_INTERVAL

network_input_speed_total = []
network_output_speed_total = []
interfaces = psutil.net_io_counters(pernic=True).keys()
network_input_speed_per = {interface: [] for interface in interfaces}
network_output_speed_per = {interface: [] for interface in interfaces}


def _get_network_io_speed():
    network_input_speed_total.append(psutil.net_io_counters().bytes_recv)
    network_output_speed_total.append(psutil.net_io_counters().bytes_sent)
    for interface in interfaces:
        network_input_speed_per[interface].append(
            psutil.net_io_counters(pernic=True)[interface].bytes_recv
        )
        network_output_speed_per[interface].append(
            psutil.net_io_counters(pernic=True)[interface].bytes_sent
        )
    while True:
        network_input_speed_total.append(
            psutil.net_io_counters().bytes_recv - network_input_speed_total[0]
        )
        network_output_speed_total.append(
            psutil.net_io_counters().bytes_sent - network_output_speed_total[0]
        )
        for interface in interfaces:
            network_input_speed_per[interface].append(
                psutil.net_io_counters(pernic=True)[interface].bytes_recv
                - network_input_speed_per[interface][0]
            )
            network_output_speed_per[interface].append(
                psutil.net_io_counters(pernic=True)[interface].bytes_sent
                - network_output_speed_per[interface][0]
            )
        sleep(NETWORK_INTERVAL)


def get_network_io_speed():
    input = [network_input_speed_total[1]]
    input += [
        network_input_speed_total[index] - network_input_speed_total[index - 1]
        for index in range(2, len(network_input_speed_total))
    ]
    output = [network_output_speed_total[1]]
    output += [
        network_output_speed_total[index] - network_output_speed_total[index - 1]
        for index in range(2, len(network_output_speed_total))
    ]
    return input, output
