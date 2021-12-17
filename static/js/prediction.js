var displayDataButton = document.getElementById('displayData');
var temperatureData = [];
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

if (dd < 10) {
    dd = '0' + dd;
}

if (mm < 10) {
    mm = '0' + mm;
}

var startDate = yyyy + '-' + mm + '-' + dd;

// get date 7 days from today
var date = new Date();
date.setDate(date.getDate() + 7);
var dd = date.getDate();
var mm = date.getMonth() + 1; //January is 0!
var yyyy = date.getFullYear();

if (dd < 10) {
    dd = '0' + dd;
}

if (mm < 10) {
    mm = '0' + mm;
}

var endDate = yyyy + '-' + mm + '-' + dd;

predictData(startDate, endDate, 1018, 'Buffalo');

displayDataButton.addEventListener('click', e => {
    e.preventDefault();
    var cityId = document.getElementById('citySearch').getAttribute('data-city-id');
    var cityName = document.getElementById('citySearch').value;
    var latitude = document.getElementById('citySearch').getAttribute('latitude');
    var longitude = document.getElementById('citySearch').getAttribute('longitude');
    predictData(startDate, endDate, cityId, cityName, latitude, longitude);
})

function predictData(startDate, endDate, cityId, cityName, latitude, longitude) {
    latitude ? latitude : latitude = 42.8864;
    longitude ? longitude : longitude = -78.8784;
    var startDateValue = startDate;
    var endDateValue = endDate;
    if (startDateValue == '' || endDateValue == '') {
        alert('Please enter a start and end date');
    } else if (endDateValue < startDateValue) {
        alert('Please enter a valid date range');
    } else {
        displayDataButton.classList.add('hidden');
        document.getElementById("processingButton").classList.remove('hidden');
        document.getElementById('predictionImage').innerHTML = "";
        $.post("/receiveDates", {
            start_date: startDateValue,
            end_date: endDateValue,
            city_id: cityId
        }, data => {
            var x = data.x_data;

            var y = data.y_data.map(function (item) {
                return Math.round(item * 100) / 100;
            });

            temperatureData = y;

            var upperBound = data.upper_bound.map(function (item) {
                return Math.round(item * 100) / 100;
            });
            var lowerBound = data.lower_bound.map(function (item) {
                return Math.round(item * 100) / 100;
            });

            var trace1 = {
                x: x,
                y: lowerBound,
                line: { width: 1 },
                mode: "lines",
                name: "Lower Bound",
                type: "scatter",
                line: { color: "#ffbf00" }
            };

            var trace2 = {
                x: x,
                y: y,
                type: "scatter",
                fillcolor: "rgba(231,107,243,0.0)",
                mode: "lines",
                fill: "tozerox",
                line: { color: "#ff8000" },
                name: "Prediction"
            };

            var trace3 = {
                x: x,
                y: upperBound,
                line: { width: 1 },
                mode: "lines",
                name: "Upper Bound",
                type: "scatter",
                line: { color: "#ff4000" }
            };

            var data = [trace1, trace2, trace3];
            var layout = {
                showlegend: true,
                xaxis: {
                    type: 'date',
                    title: 'Date'
                },
                yaxis: {
                    title: 'Daily Mean Temperature (˚C)'
                },
                title: '7 Day Weather Forecast for ' + cityName
            };

            Plotly.newPlot('predictionImage', data, layout);

            document.getElementById("processingButton").classList.add('hidden');
            displayDataButton.classList.remove('hidden');

            document.getElementById('rangeContainer').classList.remove('hidden');
            changeColor({
                city: cityName,
                latitude: latitude,
                longitude: longitude
            }, temperatureData[0])
        });
    }
}