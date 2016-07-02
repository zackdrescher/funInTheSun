
// Stores the data values for the bars
var data = [4, 8, 15, 16, 23, 42];

var x = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, 420]);

d3.select("body").selectAll("p")
    .data(data)
  .enter().append("p")
    .text(function(d, i) { return d + " " + i + " " + x;});
