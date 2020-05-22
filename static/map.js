var map = L.map("map", {
    center: [40.9631, -1.0208],
    zoom: 2
  });

// add an OpenStreetMap tile layer
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 15,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: "pk.eyJ1IjoiYmVuaXRlemFsIiwiYSI6ImNrOWZ2aTYyZDBmNG8zbGxjZ3FkZW1qYmUifQ.qh7R-7KzzMe8ikOZ1gJaaA"
}).addTo(map);
// http://127.0.0.1:5000/api/v1/alldata
var url = "http://127.0.0.1:5000/api/v1/alldata"

// d3.json(url).then(function(data) {
//   var data2 = data.filter( d => d["Data_Year"] == 2019 );
//   var country = data2[0].Country
//   console.log(data2)
//   console.log(data)
//   console.log(country)
//   // console.log('bob')
// })



//   // Create a new choropleth layer
//   geojson = L.choropleth(data2, {

//     // Define what  property in the features to use
//     valueProperty: "Happiness Score",

//     // Set color scale
//     scale: ["#ffffb2", "#b10026"],

//     // Number of breaks in step range
//     steps: 10,

//     // q for quartile, e for equidistant, k for k-means
//     mode: "q",
//     style: {
//       // Border color
//       color: "#fff",
//       weight: 1,
//       fillOpacity: 0.8
//     },


//     // Binding a pop-up to each layer
//     onEachFeature: function(feature, layer) {
//       layer.bindPopup("Zip Code: " + 2 + "<br>Median Household Income:<br>" +
//         "$" + 2);
//     }
//   }).addTo(myMap);
// });

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