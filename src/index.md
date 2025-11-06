<div style="text-align: center;">
Warriors 2015-2016 Regular Season Shot Chart<br>
Highlight an Area to see Make Percentages in that Region<br>
Source/Write Up: https://github.com/Smpramuk/CSC477_Asgn5<br> 
</div>

```js
const shotsData = await FileAttachment("warriors_2016_shots.json").json();

// Court dimensions in inches
const courtWidth = 50 * 12; // 600 inches
const halfCourtLength = 47 * 12; // 564 inches

const xMin = -courtWidth / 2; // -300
const xMax = courtWidth / 2; // 300

const baselineOffset = -48; // baseline is 4 ft behind hoop
const yMin = baselineOffset; // baseline
const yMax = halfCourtLength; // midcourt

// Chart Dimensions
const width = 700;
const height = 650;

const x = d3.scaleLinear().domain([xMin, xMax]).range([0, width]);

const y = d3.scaleLinear().domain([yMin, yMax]).range([height, 0]); // flip y so hoop is at the bottom

// COURT
const svg = d3
  .create("svg")
  .attr("width", width)
  .attr("height", height)
  .style("background", "#f8e6b7")
  .style("display", "block")
  .style("margin", "auto");

// ----- Backboard -----
const backboardY = -12;

// ----- Support arms (connecting hoop to backboard), ends up overlayed by shots
svg
  .append("line")
  .attr("x1", x(-4)) // slightly left of hoop
  .attr("y1", y(-2.8))
  .attr("x2", x(-4))
  .attr("y2", y(backboardY))
  .attr("stroke", "gray")
  .attr("stroke-width", 2);

svg
  .append("line")
  .attr("x1", x(4)) // slightly right of hoop
  .attr("y1", y(-2.8))
  .attr("x2", x(4))
  .attr("y2", y(backboardY))
  .attr("stroke", "gray")
  .attr("stroke-width", 2);

// Sidelines, baseline
svg
  .append("line")
  .attr("x1", x(-300))
  .attr("y1", y(baselineOffset))
  .attr("x2", x(300))
  .attr("y2", y(baselineOffset))
  .attr("stroke", "black")
  .attr("stroke-width", 8);
svg
  .append("line")
  .attr("x1", x(-300))
  .attr("y1", y(yMin))
  .attr("x2", x(-300))
  .attr("y2", y(yMax))
  .attr("stroke", "black")
  .attr("stroke-width", 8);
svg
  .append("line")
  .attr("x1", x(300))
  .attr("y1", y(yMin))
  .attr("x2", x(300))
  .attr("y2", y(yMax))
  .attr("stroke", "black")
  .attr("stroke-width", 8);

svg
  .append("line")
  .attr("x1", x(-300))
  .attr("y1", y(yMax))
  .attr("x2", x(300))
  .attr("y2", y(yMax))
  .attr("stroke", "black")
  .attr("stroke-width", 8);

// Curved connector between rim and backboard
svg
  .append("path")
  .attr(
    "d",
    d3.line().curve(d3.curveBasis)([
      [x(-4), y(-2.8)],
      [x(0), y(backboardY - 1.5)],
      [x(4), y(-2.8)],
    ])
  )
  .attr("stroke", "gray")
  .attr("fill", "none")
  .attr("stroke-width", 2);
// halfcourt circle
svg
  .append("circle")
  .attr("cx", x(0))
  .attr("cy", y(yMax))
  .attr("r", 72)
  .attr("stroke", "black")
  .attr("stroke-width", 2)
  .attr("fill", "none");

//  Warriors logo inside the circle
svg
  .append("image")
  .attr(
    "xlink:href",
    "https://1000logos.net/wp-content/uploads/2018/03/Golden-State-Warriors-logo.png"
  )
  .attr("x", x(0) - 360 / 2)
  .attr("y", y(yMax) - 360 / 2)
  .attr("width", 360)
  .attr("height", 360);

// ----- Hoop -----
svg
  .append("circle")
  .attr("cx", x(0))
  .attr("cy", y(0))
  .attr("r", 7)
  .attr("stroke", "orange")
  .attr("stroke-width", 2)
  .attr("fill", "none");

// Main backboard line
svg
  .append("line")
  .attr("x1", x(-36)) // half width = 72/2
  .attr("y1", y(backboardY))
  .attr("x2", x(36))
  .attr("y2", y(backboardY))
  .attr("stroke", "black")
  .attr("stroke-width", 3);

const laneWidth = 192;
const freeThrowFromBaseline = 180;
const ftRadius = 72;

// Vertical lines (paint edges)
svg
  .append("line")
  .attr("x1", x(-laneWidth / 2))
  .attr("y1", y(baselineOffset))
  .attr("x2", x(-laneWidth / 2))
  .attr("y2", y(freeThrowFromBaseline))
  .attr("stroke", "black")
  .attr("stroke-width", 3);

svg
  .append("line")
  .attr("x1", x(laneWidth / 2))
  .attr("y1", y(baselineOffset))
  .attr("x2", x(laneWidth / 2))
  .attr("y2", y(freeThrowFromBaseline))
  .attr("stroke", "black")
  .attr("stroke-width", 3);

// Free throw circle
// Top half (solid)
svg
  .append("path")
  .attr(
    "d",
    d3
      .arc()
      .innerRadius(ftRadius)
      .outerRadius(ftRadius)
      .startAngle(-Math.PI / 2)
      .endAngle(Math.PI / 2)
  )
  .attr("transform", `translate(${x(0)},${y(freeThrowFromBaseline)})`)
  .attr("stroke", "black")
  .attr("stroke-width", 2)
  .attr("fill", "none");

// Bottom half (dashed)
svg
  .append("path")
  .attr(
    "d",
    d3
      .arc()
      .innerRadius(ftRadius)
      .outerRadius(ftRadius)
      .startAngle(Math.PI / 2)
      .endAngle(1.5 * Math.PI)
  )
  .attr("transform", `translate(${x(0)},${y(freeThrowFromBaseline)})`)
  .attr("stroke", "black")
  .attr("stroke-width", 2)
  .attr("fill", "none")
  .attr("stroke-dasharray", "6,6");

// Free throw line
svg
  .append("line")
  .attr("x1", x(-laneWidth / 2))
  .attr("y1", y(freeThrowFromBaseline))
  .attr("x2", x(laneWidth / 2))
  .attr("y2", y(freeThrowFromBaseline))
  .attr("stroke", "black")
  .attr("stroke-width", 3);

const restrictedRadius = 48; // 4 ft

//Restricted circle

svg
  .append("path")
  .attr(
    "d",
    d3
      .arc()
      .innerRadius(restrictedRadius)
      .outerRadius(restrictedRadius)
      .startAngle(-Math.PI / 2) // left side
      .endAngle(Math.PI / 2) // right side
  )
  .attr("transform", `translate(${x(0)},${y(0)})`)
  .attr("stroke", "black")
  .attr("stroke-width", 3)
  .attr("fill", "none");

const threePtRadius = 285; // 285 inches
const threePtCornerX = 220; // 22 ft from 0
const threePtCornerY = 14 * 12 - 48;
const hoopY = -baselineOffset; // 48 inches above baseline

// Left corner straight line
svg
  .append("line")
  .attr("x1", x(-threePtCornerX))
  .attr("y1", y(baselineOffset)) // baseline
  .attr("x2", x(-threePtCornerX))
  .attr("y2", y(threePtCornerY - 3))
  .attr("stroke", "black")
  .attr("stroke-linecap", "round")
  .attr("stroke-width", 3);

// Right corner straight line
svg
  .append("line")
  .attr("x1", x(threePtCornerX))
  .attr("y1", y(baselineOffset))
  .attr("x2", x(threePtCornerX))
  .attr("y2", y(threePtCornerY - 3))
  .attr("stroke", "black")
  .attr("stroke-linecap", "round")
  .attr("stroke-width", 3);

//Top of key three point arc
svg
  .append("path")
  .attr(
    "d",
    d3
      .arc()
      .innerRadius(threePtRadius)
      .outerRadius(threePtRadius)
      .startAngle(-1.121) // negative for left side, angles calculated statically according to the visualization, issues with dynamic calculation
      .endAngle(1.121) // positive for right side
  )
  .attr("transform", `translate(${x(0)},${y(0)})`)
  .attr("stroke", "black")
  .attr("stroke-width", 3)
  .attr("fill", "none");

//Shots
svg
  .append("g")
  .selectAll("circle")
  .data(shotsData)
  .join("circle")
  .attr("class", "shot") //class for selection via brush if want to highlight selected points
  .attr("cx", (d) => x(d.LOC_X))
  .attr("cy", (d) => y(d.LOC_Y * 1.13))
  .attr("r", 3)
  .attr("fill", (d) => (d.SHOT_MADE_FLAG ? "green" : "red"))
  .attr("opacity", 0.6);

// Add brush behavior
// Div for the popup, hidden
const popup = d3
  .select("body")
  .append("div")
  .attr("id", "brush-popup")
  .style("position", "absolute")
  .style("padding", "8px 12px")
  .style("background", "rgba(0,0,0,0.8)")
  .style("color", "white")
  .style("border-radius", "4px")
  .style("font-family", "sans-serif")
  .style("pointer-events", "none") // ignore mouse events
  .style("opacity", 0); // hidden initially

// Brush behavior
const brush = d3
  .brush()
  .extent([
    [0, 0],
    [width, height],
  ])
  .on("start brush", () => {
    // Hide popup whenever brush starts or is being moved
    popup.transition().duration(100).style("opacity", 0);
  })
  .on("end", (event) => {
    if (!event.selection) {
      popup.transition().duration(200).style("opacity", 0); // hide if no selection
      return;
    }

    const [[x0, y0], [x1, y1]] = event.selection;

    const xMinBrush = x.invert(x0);
    const xMaxBrush = x.invert(x1);
    const yMinBrush = y.invert(y1);
    const yMaxBrush = y.invert(y0);

    const shotsInRegion = shotsData.filter(
      (d) =>
        d.LOC_X >= xMinBrush &&
        d.LOC_X <= xMaxBrush &&
        d.LOC_Y * 1.13 >= yMinBrush &&
        d.LOC_Y * 1.13 <= yMaxBrush
    );

    const totalShots = shotsInRegion.length;
    const madeShots = shotsInRegion.filter((d) => d.SHOT_MADE_FLAG).length;
    const makePercentage = totalShots > 0 ? (madeShots / totalShots) * 100 : 0;

    popup
      .html(
        `Shots in region: ${totalShots}<br>` +
          `Made shots: ${madeShots}<br>` +
          `Make %: ${makePercentage.toFixed(1)}%`
      )
      .style("left", `${event.sourceEvent.pageX + 10}px`)
      .style("top", `${event.sourceEvent.pageY + 10}px`)
      .transition()
      .duration(200)
      .style("opacity", 1); // fade in
  });

// Append brush to SVG
svg
  .append("g")
  .attr("class", "brush")
  .call(brush)
  .selectAll(".selection")
  .attr("fill", "rgba(0,0,255,0.1)")
  .attr("stroke", "blue")
  .attr("stroke-width", 1);

// Display
display(svg.node());
```
