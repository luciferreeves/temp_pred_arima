var map;
InitializeMap({
    city: "Buffalo",
    latitude: 42.8864,
    longitude: -78.8784
});

function InitializeMap(city) {
    map = L.map('map').setView([city.latitude, city.longitude], 12);
    displayMap(map, city);
}

function reRenderMap(city, style={}) {
    map.remove();
    map = L.map('map').setView([city.latitude, city.longitude], 12);
    displayMap(map, city, style);
}

function displayMap(map, city, style = {}) {
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        accessToken: 'pk.eyJ1IjoibHVjaWZlcmNyIiwiYSI6ImNrNGx0amIzejJkaHIzZm8yODB2dGx2cXYifQ.sopB-tKzpX_qXc30bv_puQ'
    }).addTo(map);
    getBoundaries(city.city).then(function (bd) {
        var lines = [];
        for (var element of bd) {
            const extractedBoundary = {
                type: 'Feature',
                properties: {
                    name: city.city
                },
                geometry: {
                    type: element.gs_type,
                    coordinates: element.boundaries.coordinates
                }
            }
            lines.push(extractedBoundary);
        }

        var geoJSON = {
            type: 'FeatureCollection',
            features: lines
        };
        var fg = L.featureGroup().addTo(map);
        var gs = L.geoJSON(geoJSON).addTo(map);

        if (style.fillColor) {
            fg.clearLayers();
            gs.setStyle(style);
        }

        try {
            map.fitBounds(gs.getBounds());
        } catch (e) {
            L.marker([city.latitude, city.longitude]).addTo(map)
                .bindPopup(city.city)
                .openPopup();
        }
    })
}

function getBoundaries(city) {
    geojson = [];

    return fetch(`https://nominatim.openstreetmap.org/search.php?q=${city}&polygon_geojson=1&format=jsonv2`).then(function (response) {
        return response.json();
    }).then(function (data) {
        counter = 0;

        for (var el of data) {
            if (el.type === "administrative") {
                geojson.push({ boundaries: el.geojson, name: el.display_name, gs_type: el.geojson.type });
                counter += 1;
            }

            if (counter === 1 && !el.display_name.includes("Rural")) {
                break;
            } else if (counter === 2 && el.display_name.includes("Rural")) {
                break;
            }
        }
        return geojson;
    }).catch(function () {
        return false;
    });
}

function getColors(temperature) {
    // Generate relevant colors from temperature values for the map and return them
    // Set hex values to 0.3 opacity
    return temperature > 40 ? '#ff0000' : temperature > 30 ? '#ff4000' : temperature > 20 ? '#ff8000' : temperature > 10 ? '#ffbf00' : temperature > 0 ? '#ffff00' : temperature > -10 ? '#bfff00' : temperature > -20 ? '#80ff00' : temperature > -30 ? '#40ff00' : temperature > -40 ? '#00ff00' : '#00ff40';
}

// Function to change color of the map geoJSON based on provided temperature input
function changeColor(city, temperature) {
    var color = getColors(temperature);
    var style = {
        fillColor: color,
        fillOpacity: 0.3,
        color: color,
        weight: 1
    };
    reRenderMap(city, style);
}

