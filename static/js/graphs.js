function onGraphLoad() {
	progressstats();
	progressstats1();
	dailystats();
	weeklystats();
	monthlystats();
}

function progressstats1() {
    // The data held in javascript
    var data = []
    // AJAX http request
    var xmlhttp = new XMLHttpRequest();

    // Callback function for successfull AJAX request

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Retrieved JSON content successful. Now parse to native javascript format
            data = JSON.parse(this.responseText);
			
            // Use adequate size for all devices and calculate radius
            var width = 300,
                height = 300,
                radius = Math.min(width, height) / 2;

            // Allocate random colouring scheme for different  items
            var color = d3.scaleOrdinal(d3.schemeCategory10);

            // Supply the data for the pie chart
            var pie = d3.pie().value(function (d) {
					
                return d.amount;
            })(data);

            // Generate arc
            var arc = d3.arc().outerRadius(radius - 10).innerRadius(0);

            // Generate label for arc
            var labelArc = d3.arc().outerRadius(radius - 40).innerRadius(radius - 40);

            // Generate SVG item and transform and translate it.
            var svg = d3.select("#progressstats1").append("svg").attr("width", width).attr("height", height).append("g")
                .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

            var g = svg.selectAll("arc").data(pie).enter().append("g")
                .attr("class", "arc");

            // Fill the specific course item with a colour
            g.append("path").attr("d", arc).style("fill", function (d) {
                return colorPicker(d.data.progress);
            });

            // Add the text label
            g.append("text").attr("transform", function (d) {
                var centroid = arc.centroid(d);
				d3.select(this)
					.attr('x', centroid[0])
					.attr('y', centroid[1])
					.attr('dy', '0.33em')
					.text(d.label);
	
            }).text(function (d) {
                return d.data.progress;
            })
                .style("fill", "#fff");

        }
    };
    // Retrieve AJAX stats from backend
    xmlhttp.open("GET", "/graphs/progressstats", true);
    xmlhttp.send();
}

function colorPicker(v) {
	
  if (v == "TODO") {
    return "red";
  } else if (v == "DONE") {
    return "green";
  } else {
	  return "orange";
  }
}

function progressstats() {
    // The data held in javascript
    var data = []
    // The AJAX request
    var xmlhttp = new XMLHttpRequest();

    // Callback function for successfull AJAX request
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Retrieved JSON content successful. Now parse to native javascript format
            data = JSON.parse(this.responseText);

            // The margin for the bar chart
            var margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 40
            },

                // Calculate the width and height using an adequate size for all devices
                width = 360 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;

            // Random colour scheme
            var color = d3.scaleOrdinal(d3.schemeCategory10);


            var x = d3.scaleBand()
                .range([0, width])
                .padding(0.1);
            var y = d3.scaleLinear()
                .range([height, 0]);

            // Calculate SVG item transform and translate it.
            var svg = d3.select("#progressstats").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            // The data for the x axis
            x.domain(data.map(function (d) {
                return d.progress;
            }));

            // The data for the y axis
            y.domain([0, d3.max(data, function (d) {
                return d.amount;
            })]);

            // append the rectangles for the bar chart
            svg.selectAll(".bar")
                .data(data)
                .enter().append("rect")
                .attr("class", "bar")
                .attr("x", function (d) {
                    return x(d.progress);
                })
                .attr("width", x.bandwidth())
                .attr("y", function (d) {
                    return y(d.amount);
                })
                .attr("height", function (d) {
                    return height - y(d.amount);
                })
                .attr("fill", function (d) {
                    return colorPicker(d.progress);
                });

            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            svg.append("g")
                .call(d3.axisLeft(y).ticks(10));

        };
    }
    // AJAX Request
    xmlhttp.open("GET", "/graphs/progressstats", true);
    xmlhttp.send();
}

function dailystats() {
    // The data held in javascript
    var data = []
    // The AJAX request
    var xmlhttp = new XMLHttpRequest();

    // Callback function for successfull AJAX request
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Retrieved JSON content successful. Now parse to native javascript format
            data = JSON.parse(this.responseText);

            // The margin for the bar chart
            var margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 40
            },

                // Calculate the width and height using an adequate size for all devices
                width = 360 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;

            // Random colour scheme
            var color = d3.scaleOrdinal(d3.schemeCategory10);


            var x = d3.scaleBand()
                .range([0, width])
                .padding(0.1);
            var y = d3.scaleLinear()
                .range([height, 0]);

            // Calculate SVG item transform and translate it.
            var svg = d3.select("#dailystats").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            // The data for the x axis
            x.domain(data.map(function (d) {
                return d.day;
            }));

            // The data for the y axis
            y.domain([0, d3.max(data, function (d) {
                return d.amount;
            })]);

            // append the rectangles for the bar chart
            svg.selectAll(".bar")
                .data(data)
                .enter().append("rect")
                .attr("class", "bar")
                .attr("x", function (d) {
                    return x(d.day);
                })
                .attr("width", x.bandwidth())
                .attr("y", function (d) {
                    return y(d.amount);
                })
                .attr("height", function (d) {
                    return height - y(d.amount);
                })
                .attr("fill", function (d) {
                    return color(d.day);
                });

            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            svg.append("g")
                .call(d3.axisLeft(y).ticks(1));

        };
    }
    // AJAX Request
    xmlhttp.open("GET", "/graphs/dailystats", true);
    xmlhttp.send();
}

function weeklystats() {
    // The data held in javascript
    var data = []
    // The AJAX request
    var xmlhttp = new XMLHttpRequest();

    // Callback function for successfull AJAX request
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Retrieved JSON content successful. Now parse to native javascript format
            data = JSON.parse(this.responseText);

            // The margin for the bar chart
            var margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 40
            },

                // Calculate the width and height using an adequate size for all devices
                width = 360 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;

            // Random colour scheme
            var color = d3.scaleOrdinal(d3.schemeCategory10);


            var x = d3.scaleBand()
                .range([0, width])
                .padding(0.1);
            var y = d3.scaleLinear()
                .range([height, 0]);

            // Calculate SVG item transform and translate it.
            var svg = d3.select("#weeklystats").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            // The data for the x axis
            x.domain(data.map(function (d) {
                return d.week;
            }));

            // The data for the y axis
            y.domain([0, d3.max(data, function (d) {
                return d.amount;
            })]);

            // append the rectangles for the bar chart
            svg.selectAll(".bar")
                .data(data)
                .enter().append("rect")
                .attr("class", "bar")
                .attr("x", function (d) {
                    return x(d.week);
                })
                .attr("width", x.bandwidth())
                .attr("y", function (d) {
                    return y(d.amount);
                })
                .attr("height", function (d) {
                    return height - y(d.amount);
                })
                .attr("fill", function (d) {
                    return color(d.week);
                });

            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            svg.append("g")
                .call(d3.axisLeft(y).ticks(1));

        };
    }
    // AJAX Request
    xmlhttp.open("GET", "/graphs/weeklystats", true);
    xmlhttp.send();
}



function monthlystats() {
    // The data held in javascript
    var data = []
    // The AJAX request
    var xmlhttp = new XMLHttpRequest();

    // Callback function for successfull AJAX request
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Retrieved JSON content successful. Now parse to native javascript format
            data = JSON.parse(this.responseText);

            // The margin for the bar chart
            var margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 40
            },

                // Calculate the width and height using an adequate size for all devices
                width = 360 - margin.left - margin.right,
                height = 300 - margin.top - margin.bottom;

            // Random colour scheme
            var color = d3.scaleOrdinal(d3.schemeCategory10);


            var x = d3.scaleBand()
                .range([0, width])
                .padding(0.1);
            var y = d3.scaleLinear()
                .range([height, 0]);

            // Calculate SVG item transform and translate it.
            var svg = d3.select("#monthlystats").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            // The data for the x axis
            x.domain(data.map(function (d) {
                return d.month;
            }));

            // The data for the y axis
            y.domain([0, d3.max(data, function (d) {
                return d.amount + 1;
            })]);

            // append the rectangles for the bar chart
            svg.selectAll(".bar")
                .data(data)
                .enter().append("rect")
                .attr("class", "bar")
                .attr("x", function (d) {
                    return x(d.month);
                })
                .attr("width", x.bandwidth())
                .attr("y", function (d) {
                    return y(d.amount);
                })
                .attr("height", function (d) {
                    return height - y(d.amount);
                })
                .attr("fill", function (d) {
                    return color(d.month);
                });

            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x));

            svg.append("g")
                .call(d3.axisLeft(y).ticks(1));

        };
    }
    // AJAX Request
    xmlhttp.open("GET", "/graphs/monthlystats", true);
    xmlhttp.send();
}

