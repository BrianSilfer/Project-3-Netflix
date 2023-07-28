
  
  //bb version
  var chart = bb.generate({
    data: {
      columns: [
    ["data1", 30],
    ["data2", 120]
      ],
      type: "pie",
      onclick: function(d, i) {
    console.log("onclick", d, i);
     },
      onover: function(d, i) {
    console.log("onover", d, i);
     },
      onout: function(d, i) {
    console.log("onout", d, i);
     }
    },
    bindto: "#pieChart"

    //plotly version
    var data = [{
      values: [11, 429, 1188, 1649, 1905,    ],
      labels: ['2015', '2016', '2017', '2018', '2019'],
      type: 'pie'
      hoverinfo: 'value'
    }];
    var layout = {
      height: 400,
      width: 500,
      title: 'Number of Premiers Per Year'
    
    };
    
    
    Plotly.newPlot('myDiv', data, layout);
    
  });
  
  
}
  
    
  

    
  init();