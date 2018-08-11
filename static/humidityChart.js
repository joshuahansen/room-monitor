console.log(data)

let points = []

for(let i = 0; i < data.length; ++i) {
	let date = new Date(data[i][0])
	//x is hours
	let x = date.getMinutes()
	//y is humidity
	let y = data[i][2]
	points.push({x: x, y: y})
}
let ctx = document.getElementById('humidityChart').getContext('2d')
let chart = new Chart(ctx, {
	type: 'line',
	data: points,
	options: {
		responsive: true,
		title: {
			display: true,
			text: "Humidity Readingd for the past 24 hours"
		}
	}
});
