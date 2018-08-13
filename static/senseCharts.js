let humidityPoints = []
let temperaturePoints = []
let labels = []

for(let i = 0; i < data.length; ++i) {
	let date = new Date(data[i][0])
	let hours = date.getHours()
	let mins = date.getMinutes()

	let time = hours
	
	let temperature = data[i][1]
	let humidity = data[i][2]

	humidityPoints.push({x: time, y: humidity})
	temperaturePoints.push({x: time, y: temperature})

	hours < 10 ? hours = "0" + hours : hours
	mins < 10 ? mins = "0" + mins : mins
	labels.push(hours + ":" + mins)

}
new Chart($('#humidityChart'), {
	'type': 'line',
	'data': {
		'labels': labels,
		'datasets': [{
			'label': "Humidity",
			'data': humidityPoints,
			'fill': false,
			'borderColor': "rgb(75, 192, 192)",
			'lineTension': 0.1,
		}]
	},
	'options': {
		'responsive': true,
		'title': {
			'display': true,
			'text': "Humidity readings for the past 24 hours"
		}
	}
});

new Chart($('#temperatureChart'), {
	'type': 'line',
	'data': {
		'labels': labels,
		'datasets': [{
			'label': "Temperature",
			'data': temperaturePoints,
			'fill': false,
			'borderColor': "rgb(255, 0, 0)",
			'lineTension': 0.1,
		}]
	},
	'options': {
		'responsive': true,
		'title': {
			'display': true,
			'text': "Temperature readings for the past 24 hours"
		}
	}
});
