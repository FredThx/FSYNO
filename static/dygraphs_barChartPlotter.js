//Pour DyGraphs
// Aficher le graphe sous forme de barres
//
// usage : 
/* 			g = new Dygraph(
              document.getElementById("test"),
              "Date,Widgets Sold\n" +
              "2012/07/21,10\n" +
				....
              "2012/07/25,10\n",
              {
                legend: 'always',
				...
                plotter: barChartPlotter // ICI
              }
          ); */


// Darken a color
  function darkenColor(colorStr) {
	// Defined in dygraph-utils.js
	var color = Dygraph.toRGB_(colorStr);
	color.r = Math.floor((255 + color.r) / 2);
	color.g = Math.floor((255 + color.g) / 2);
	color.b = Math.floor((255 + color.b) / 2);
	return 'rgb(' + color.r + ',' + color.g + ',' + color.b + ')';
  }

  // This function draws bars for a single series. See
  // multiColumnBarPlotter below for a plotter which can draw multi-series
  // bar charts.
  function barChartPlotter(e) {
	var ctx = e.drawingContext;
	var points = e.points;
	var y_bottom = e.dygraph.toDomYCoord(0);

	ctx.fillStyle = darkenColor(e.color);

	// Find the minimum separation between x-values.
	// This determines the bar width.
	var min_sep = Infinity;
	for (var i = 1; i < points.length; i++) {
	  var sep = points[i].canvasx - points[i - 1].canvasx;
	  if (sep < min_sep) min_sep = sep;
	}
	var bar_width = Math.floor(2.0 / 3 * min_sep);

	// Do the actual plotting.
	for (var i = 0; i < points.length; i++) {
	  var p = points[i];
	  var center_x = p.canvasx;

	  ctx.fillRect(center_x - bar_width / 2, p.canvasy,
		  bar_width, y_bottom - p.canvasy);

	  ctx.strokeRect(center_x - bar_width / 2, p.canvasy,
		  bar_width, y_bottom - p.canvasy);
	}
  }
