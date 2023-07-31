const stocksData = "http://127.0.0.1:5000/stocks";
const movieData = "http://127.0.0.1:5000/movies";
// 2015
const stocksData15 = "http://127.0.0.1:5000/stocks/date/start=2014/stop=2015";
const movieData15 = "http://127.0.0.1:5000/movies/added/start=2014/stop=2015";
// 2016
const stocksData16 = "http://127.0.0.1:5000/stocks/date/start=2015/stop=2016";
const movieData16 = "http://127.0.0.1:5000/movies/added/start=2015/stop=2016";
// 2017
const stocksData17 = "http://127.0.0.1:5000/stocks/date/start=2016/stop=2017";
const movieData17 = "http://127.0.0.1:5000/movies/added/start=2016/stop=2017";
// 2018
const stocksData18 = "http://127.0.0.1:5000/stocks/date/start=2017/stop=2018";
const movieData18 = "http://127.0.0.1:5000/movies/added/start=2017/stop=2018";
// 2019
const stocksData19 = "http://127.0.0.1:5000/stocks/date/start=2018/stop=2019";
const movieData19 = "http://127.0.0.1:5000/movies/added/start=2018/stop=2019";


function init() {

Promise.all([
  d3.json(stocksData),
  d3.json(movieData)
]).then(function([stocksData, movieData]){
  console.log(stocksData,movieData);

var trace1 = {
  x: stocksData.map(row => row.Date),
  y: stocksData.map(row => row.High),
  mode: 'markers+lines',
  type: 'scatter',
  text:(movieData.map(row => row.title)),
  marker: { size: 12 }
};

let traceData = [trace1];
var layout = {showlegend: false};
Plotly.newPlot("plot", traceData,layout);
});
}

d3.selectAll("#selDataset").on("change", updatePlotly);

function updatePlotly(){
  // Use D3 to select the dropdown menu
  let dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  let dataset = dropdownMenu.property("value");

let x = [];
let y = [];

Promise.all([
  d3.json(stocksData15),
  d3.json(stocksData16),
  d3.json(stocksData17),
  d3.json(stocksData18),
  d3.json(stocksData19),
  d3.json(movieData15),
  d3.json(movieData16),
  d3.json(movieData17),
  d3.json(movieData18),
  d3.json(movieData19)
]).then(function([stocksData15,stocksData16,stocksData17,stocksData18,stocksData19,movieData15,movieData16,movieData17,movieData18,movieData19]){

  console.log(stocksData15,stocksData16,stocksData17,stocksData18,stocksData19,movieData15,movieData16,movieData17,movieData18,movieData19);


if (dataset === '2015') {
  x = stocksData15.map(row => row.Date),
  y = stocksData15.map(row => row.High),
  text = (movieData15.map(row => row.title));
}

if (dataset === '2016') {
  x = stocksData16.map(row => row.Date),
  y = stocksData16.map(row => row.High),
  text = (movieData16.map(row => row.title));
}

if (dataset === '2017') {
  x = stocksData17.map(row => row.Date),
  y = stocksData17.map(row => row.High),
  text = (movieData17.map(row => row.title));
}

if (dataset === '2018') {
  x = stocksData18.map(row => row.Date),
  y = stocksData18.map(row => row.High),
  text = (movieData18.map(row => row.title));
}

else if (dataset === '2019') {
  x = stocksData19.map(row => row.Date),
  y = stocksData19.map(row => row.High),
  text = (movieData19.map(row => row.title));
}

Plotly.restyle("plot", "x", [x]);
Plotly.restyle("plot", "y", [y]);

});


}



init();
