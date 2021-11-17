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

function reRenderMap(city) {
    map.remove();
    map = L.map('map').setView([city.latitude, city.longitude], 12);
    displayMap(map, city);
}

function displayMap(map, city) {
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

        var gs = L.geoJSON(geoJSON).addTo(map);
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