function buildPlot() {
var url = "http://127.0.0.1:5000/api/v1/alldata"
d3.json(url).then(function(data) {
  var data1 = data;
  var data2 = data.filter( d => d["Data_Year"] == 2019 );
  var data3 = data.filter( d => d["Data_Year"] == 2018 );
  var data4 = data.filter( d => d["Data_Year"] == 2017 );
  var data5 = data.filter( d => d["Data_Year"] == 2016 );
  var data6 = data.filter( d => d["Data_Year"] == 2015 );

  var sortedByranking1 = data2.sort((a, b) => b.Happiness_Score - a.Happiness_Score);
  var sortedByranking2= data3.sort((a, b) => b.Happiness_Score - a.Happiness_Score);
  var sortedByranking3 = data4.sort((a, b) => b.Happiness_Score - a.Happiness_Score);
  var sortedByranking4 = data5.sort((a, b) => b.Happiness_Score - a.Happiness_Score);
  var sortedByranking5 = data6.sort((a, b) => b.Happiness_Score - a.Happiness_Score);

  slicedData = sortedByranking1.slice(0, 6).reverse();
  slicedData2 = sortedByranking1.slice(151,156).reverse();
  slicedData3 = sortedByranking2.slice(0,6).reverse();
  slicedData4 = sortedByranking2.slice(151,156).reverse();
  slicedData5 = sortedByranking3.slice(0,6).reverse();
  slicedData6 = sortedByranking3.slice(150,155).reverse();
  slicedData7 = sortedByranking4.slice(0,6).reverse();
  slicedData8 = sortedByranking4.slice(152,157).reverse();
  slicedData9 = sortedByranking5.slice(0,6).reverse();
  slicedData10 = sortedByranking5.slice(153,158).reverse();
var trace1 = {
  x: slicedData.map(object => object.Happiness_Score),
  y: slicedData.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(36,86,104)',
    opacity: 0.8,
  }
  }
var trace2 = {
x: slicedData2.map(object=> object.Happiness_Score),
y: slicedData2.map(object=> object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(248,181,139)',
    opacity: 0.8,
  }

}
var trace3 = {
  x: slicedData3.map(object => object.Happiness_Score),
  y: slicedData3.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(36,86,104)',
    opacity: 0.8,
}
}
var trace4 = {
  x: slicedData4.map(object => object.Happiness_Score),
  y: slicedData4.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(248,181,139)',
    opacity: 0.8,
}
}
var trace5 = {
  x: slicedData5.map(object => object.Happiness_Score),
  y: slicedData5.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(36,86,104)',
    opacity: 0.8,
}
}
var trace6 = {
  x: slicedData6.map(object => object.Happiness_Score),
  y: slicedData6.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(248,181,139)',
    opacity: 0.8,
}
}
var trace7 = {
  x: slicedData7.map(object => object.Happiness_Score),
  y: slicedData7.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(36,86,104)',
    opacity: 0.8,
}
}
var trace8 = {
  x: slicedData8.map(object => object.Happiness_Score),
  y: slicedData8.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(248,181,139)',
    opacity: 0.8,
}
}
var trace9 = {
  x: slicedData9.map(object => object.Happiness_Score),
  y: slicedData9.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(36,86,104)',
    opacity: 0.8,
}
}
var trace10 ={
  x: slicedData10.map(object => object.Happiness_Score),
  y: slicedData10.map(object => object.Country),
  type: "bar",
  orientation: "h",
  marker: {
    color: 'rgb(248,181,139)',
    opacity: 0.8,
}
}
var data = [trace2,trace1];
var layout = {
  showlegend: false,
  xaxis: {
    showgrid: true,
    showline: false,
    showticklabels: false,
  },
  margin: {
    l: 100,
    r: 10,
    t: 30,
    b: 10
  }  
}
Plotly.newPlot("bar", data, layout,{displayModeBar: false},{responsive: true});

var trace11 = {
  x: sortedByranking1.map(obj => obj.Happiness_Score).slice(0, 10),
  y: sortedByranking1.map(obj => obj.Life_Expectancy).slice(0, 10),
  text: sortedByranking1.map(obj=>obj.Country).slice(0, 10),
  name: 'Happiest countries ',
  mode: 'markers',
  marker: {
    color: 'rgb(138,29,99)',
    size: 12,
    
  }           
}
var trace12 = {
  x: sortedByranking1.map(obj => obj.Happiness_Score).slice(146,156),
  y: sortedByranking1.map(obj => obj.Life_Expectancy).slice(146,156),
  text: sortedByranking1.map(obj=>obj.Country).slice(146,156),
  name: 'Countries least happiness ',
  mode: 'markers',
  marker: {
    color: 'rgb(75,138,20)',
    size: 12,
    
  }     
}
var trace13 = {
  x: sortedByranking1.map(obj => obj.Happiness_Score).slice(11,145),
  y: sortedByranking1.map(obj => obj.Life_Expectancy).slice(11,145),
  text: sortedByranking1.map(obj=>obj.Country).slice(11,145),
  name: 'Av happiness ',
  mode: 'markers',
  marker: {
    color: 'rgb(213, 156, 137)',
    size: 12,
    
  }     
}
var layout1 = {
  height: 600,
  width: 1200,
  xaxis: {
    title: 'Happiness Ranking'
  },
  yaxis: {
    title: 'Life Expectancy'
  }
}

Plotly.newPlot("bubble", [trace11,trace12,trace13],layout1);

});
}

function getData() {
  // On change to the DOM, call getData()
  d3.selectAll("#selDataset").on("change", getData);
  
  // Function called by DOM changes
  
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
    // Initialize an empty array for the country's data
    var data = [];
  
    if (dataset == '2019') {
        data = trace2,trace1;
    }
    else if (dataset == '2018') {
        data = trace4,trace3
    }

    // Call function to update the chart
    updatePlotly(data);
  }
  // getData();
  // Update the restyled plot's values
  function updatePlotly(newdata) {
    Plotly.restyle("bar",[newdata]);
  }
  buildPlot();




