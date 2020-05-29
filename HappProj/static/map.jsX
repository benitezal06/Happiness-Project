
// World Happiness map - START
var map = L.map("map", {
    center: [40.9631, -1.0208],
    zoom: 2
  });


// add an OpenStreetMap tile layer - mapbox/streets-v11
// mapbox.streets mapbox.light mapbox.dark mapbox.satelight mapbox.streets-satelite 
// mapbox.wheatpaste mapbox.streets-basic mapbox.comic mapbox.outdoors
// mapbox.run-bike-hike mapbox.pencil mapbox.pirates mapbox.emerald mapbox.high-contrast
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom:15,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: "pk.eyJ1IjoiYmVuaXRlemFsIiwiYSI6ImNrOWZ2aTYyZDBmNG8zbGxjZ3FkZW1qYmUifQ.qh7R-7KzzMe8ikOZ1gJaaA"
}).addTo(map);


function loadMapForYear(year) {
  // load geoJsonData data
  d3.json("http://127.0.0.1:5000/api/v1/getGeoJsonData/" + year).then(function(geoJsonData) {

    // add color to the map for country rank
    L.geoJson(geoJsonData, {style: style}).addTo(map);

  });
}

// select color based on happiness rank
function chooseColor(happinessRank) {
  return happinessRank > 150 ? '#800026' :
         happinessRank > 120 ? '#BD0026' :
         happinessRank > 90  ? '#E31A1C' :
         happinessRank > 70  ? '#FC4E2A' :
         happinessRank > 50  ? '#FD8D3C' :
         happinessRank > 30  ? '#FEB24C' :
         happinessRank > 10  ? '#FED976' :
                               '#FFEDA0';
}

// style to be added to map layer for setting color to happiness rank
function style(feature) {
  return {
      fillColor: chooseColor(feature.properties.Happiness_Rank),
      weight: 2,
      opacity: 1,
      color: 'white',
      dashArray: '3',
      fillOpacity: 0.7
  };
}

// add legend
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

  var div = L.DomUtil.create('div', 'info legend'),
    ranks = [0, 10, 30, 50, 70, 90, 120, 150],
    labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < ranks.length; i++) {
      div.innerHTML +=
          '<i style="background:' + chooseColor(ranks[i] + 1) + '"></i> ' +
            ranks[i] + (ranks[i + 1] ? '&ndash;' + ranks[i + 1] + '<br>' : '+');
    }

    return div;
  };

  legend.addTo(map);



// Add  year filter
//get year options 
// var optionStr = "";
// d3.json("http://127.0.0.1:5000/getYears").then(function(years) {
// years.forEach(year => {  
//     optionStr = optionStr + "<option>" + year + "</option>";
//     console.log("loop: " + optionStr);
//   });
// });
// console.log("outside: " + optionStr);

var legend = L.control({position: 'topright'});

legend.onAdd = function (map) {
  var div = L.DomUtil.create('div', 'info legend');
  div.innerHTML = "<select  onchange='yearChangedEvent(this)'><option>All Years</option><option>2015</option><option>2016</option><option>2017</option><option>2018</option><option>2019</option></select>";
  div.firstChild.onmousedown = div.firstChild.ondblclick = L.DomEvent.stopPropagation;
  return div;
};

legend.addTo(map);


// drop down year filter selection
function yearChangedEvent(selectObject) {
  var year = selectObject.value; 
  loadMapForYear(year);
  console.log(year);
}

// set default year to All Years - first time
loadMapForYear("All Years");
// World Happiness map - END








// var trace1 = {
//   x: [1, 2, 3, 4],
//   y: [10, 15, 13, 17],
//   mode: 'markers',
//   type: 'scatter'
// };

// var trace2 = {
//   x: [2, 3, 4, 5],
//   y: [16, 5, 11, 9],
//   mode: 'lines',
//   type: 'scatter'
// };

// var trace3 = {
//   x: [1, 2, 3, 4],
//   y: [12, 9, 15, 12],
//   mode: 'lines+markers',
//   type: 'scatter'
// };

// var data = [trace1, trace2, trace3];

// Plotly.newPlot('myDiv', data);
