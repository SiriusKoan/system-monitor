const HOST = "127.0.0.1:5000";

const config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'CPU Usage',
            data: [],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1,
            fill: false,
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            }
        }
    },
};

var ctx_cpu_usage = document.getElementById("cpu_usage_canvas").getContext('2d');
var cpu_usage_chart = new Chart(ctx_cpu_usage, config);
// var ctx_memory_usage = document.getElementById("memory_usage_canvas").getContext('2d');


function getTimestamp() {
    $.ajax({
        url: `http://${HOST}/api/timestamp`,
        type: "GET",
        dataType: "json",
    }).always(function (r) {
        // console.log(r.timestamp)
        cpu_usage_chart.data.labels = r.timestamp.map(function (item) { return new Date(item * 1e3).toISOString() });
        cpu_usage_chart.update();
        setTimeout(getTimestamp, 1000);
    });
}

function getCPUUsage() {
    $.ajax({
        url: `http://${HOST}/api/cpu_usage`,
        type: "GET",
        dataType: "json",
    }).always(function (r) {
        // console.log(r)
        // console.log(cpu_usage_chart.data.datasets[0])
        cpu_usage_chart.data.datasets[0].data = r.cpu_usage_total;
        cpu_usage_chart.update();
        setTimeout(getCPUUsage, 1000);
    });
}

getTimestamp();
getCPUUsage();