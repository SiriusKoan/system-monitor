const HOST = "127.0.0.1:5000";
const TIMEZONE = 8;
const TIME_INTERVAL = 5000;
const MAX_DATA_LENGTH = 500;
const color_table = [
    'rgba(255, 99, 132, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    'rgba(255, 206, 86, 0.8)',
    'rgba(75, 192, 192, 0.8)',
    'rgba(153, 102, 255, 0.8)',
]

function createConfig(types, description, min = null, max = null) {
    datasets = []
    for (var i = 0; i < types.length; i++) {
        datasets.push({
            label: types[i],
            data: [],
            backgroundColor: color_table[i],
            borderWidth: 1,
            fill: false,
        })
    }

    const config = {
        type: "line",
        data: {
            labels: [],
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: description
                }
            },
        },
    };
    if (min != null && max != null) {
        config.options.scales = {
            y: {
                min: 0,
                max: 100,
            }
        }
    }
    return config;
}

function timestampToDate(timestamp) {
    return new Date((timestamp + TIMEZONE * 60 * 60) * 1e3).toISOString().slice(11, 19).replace('T', ' ');
}

var ctx_cpu_usage = document.getElementById("cpu_usage_canvas").getContext("2d");
var cpu_usage_chart = new Chart(ctx_cpu_usage, createConfig(["CPU Usage"], "CPU Usage Line Chart", 0, 100));
var ctx_vir_memory_usage = document.getElementById("vir_memory_usage_canvas").getContext("2d");
var vir_memory_usage_chart = new Chart(ctx_vir_memory_usage, createConfig(["Virtual Memory Usage"], "Virtual Memory Usage Line Chart", 0, 100));
var ctx_disk_io_speed = document.getElementById("disk_io_speed_canvas").getContext("2d");
var disk_io_speed_chart = new Chart(ctx_disk_io_speed, createConfig(["Read", "Write"], "Disk IO Line Chart"));
var ctx_network_io_speed = document.getElementById("network_io_speed_canvas").getContext("2d");
var network_io_speed_chart = new Chart(ctx_network_io_speed, createConfig(["Input", "Output"], "Network Speed Line Chart"));
var ctx_battey_usage = document.getElementById("battery_usage_canvas").getContext("2d");
var battery_usage_chart = new Chart(ctx_battey_usage, createConfig(["Battery Usage"], "Battery Usage Line Chart", 0, 100));


function getTimestamp() {
    $.ajax({
        url: `http://${HOST}/api/timestamp`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        timestamps = r.timestamp.map(function(time) { return timestampToDate(time) });
        cpu_usage_chart.data.labels = cpu_usage_chart.data.labels.concat(timestamps);
        vir_memory_usage_chart.data.labels = vir_memory_usage_chart.data.labels.concat(timestamps);
        disk_io_speed_chart.data.labels = disk_io_speed_chart.data.labels.concat(timestamps);
        network_io_speed_chart.data.labels = network_io_speed_chart.data.labels.concat(timestamps);
        battery_usage_chart.data.labels = battery_usage_chart.data.labels.concat(timestamps);
        cpu_usage_chart.update();
        vir_memory_usage_chart.update();
        disk_io_speed_chart.update();
        network_io_speed_chart.update();
        battery_usage_chart.update();
        setTimeout(getTimestamp, TIME_INTERVAL);
    });
}

function getCPUUsage() {
    $.ajax({
        url: `http://${HOST}/api/cpu_usage`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        cpu_usage_chart.data.datasets[0].data = cpu_usage_chart.data.datasets[0].data.concat(r.cpu_usage_total);
        cpu_usage_chart.update();
        setTimeout(getCPUUsage, TIME_INTERVAL);
    });
}

function getMemoryUsage() {
    $.ajax({
        url: `http://${HOST}/api/memory_usage`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        vir_memory_usage_chart.data.datasets[0].data = vir_memory_usage_chart.data.datasets[0].data.concat(r.vir_memory_usage_percent);
        vir_memory_usage_chart.update();
        setTimeout(getMemoryUsage, TIME_INTERVAL);
    });
}

function getDiskIOSpeed() {
    $.ajax({
        url: `http://${HOST}/api/disk_io`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        disk_io_speed_chart.data.datasets[0].data = disk_io_speed_chart.data.datasets[0].data.concat(r.disk_io_speed_total.read);
        disk_io_speed_chart.data.datasets[1].data = disk_io_speed_chart.data.datasets[1].data.concat(r.disk_io_speed_total.write);
        disk_io_speed_chart.update();
        setTimeout(getDiskIOSpeed, TIME_INTERVAL);
    });
}

function getNetworkSpeed() {
    $.ajax({
        url: `http://${HOST}/api/network_io`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        network_io_speed_chart.data.datasets[0].data = network_io_speed_chart.data.datasets[0].data.concat(r.network_io_speed_total.input);
        network_io_speed_chart.data.datasets[1].data = network_io_speed_chart.data.datasets[1].data.concat(r.network_io_speed_total.output);
        network_io_speed_chart.update();
        setTimeout(getNetworkSpeed, TIME_INTERVAL);
    });
}

function getBatteryUsage() {
    $.ajax({
        url: `http://${HOST}/api/sysinfo`,
        type: "GET",
        dataType: "json",
    }).always(function(r) {
        data = r.battery_info.map(function(info) { return info.percent });
        battery_usage_chart.data.datasets[0].data = battery_usage_chart.data.datasets[0].data.concat(data);
        battery_usage_chart.update();
        setTimeout(getBatteryUsage, TIME_INTERVAL);
    });
}

function shiftData() {
    if (cpu_usage_chart.data.labels.length > MAX_DATA_LENGTH) {
        cpu_usage_chart.data.datasets[0].data.shift();
        cpu_usage_chart.data.labels.shift();
        vir_memory_usage_chart.data.datasets[0].data.shift();
        vir_memory_usage_chart.data.labels.shift();
        disk_io_speed_chart.data.datasets[0].data.shift();
        disk_io_speed_chart.data.datasets[1].data.shift();
        disk_io_speed_chart.data.labels.shift();
        network_io_speed_chart.data.datasets[0].data.shift();
        network_io_speed_chart.data.datasets[1].data.shift();
        network_io_speed_chart.data.labels.shift();
        battery_usage_chart.data.datasets[0].data.shift();
        battery_usage_chart.data.labels.shift();
        cpu_usage_chart.update();
        vir_memory_usage_chart.update();
        disk_io_speed_chart.update();
        network_io_speed_chart.update();
        battery_usage_chart.update();
    }
    setTimeout(shiftData, 1000);
}

getTimestamp();
getCPUUsage();
getMemoryUsage();
getDiskIOSpeed();
getNetworkSpeed();
getBatteryUsage();
shiftData();