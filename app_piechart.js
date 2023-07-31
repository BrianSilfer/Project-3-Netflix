function init() {
  var trace1 = {
      values: [11, 429, 1188, 1649, 1905],
      labels: ['2015', '2016', '2017', '2018', '2019'],
      type: 'pie'
  };
  var data = [trace1];
  var layout = {
      width: 450,
      height: 400,
      margin: { t: 25, r: 25, l: 25, b: 25 },
      title: 'Number of Premiers Per Year'
    
  };
    
    
  Plotly.newPlot("pieChart", data, layout);
    
  

}    
init();