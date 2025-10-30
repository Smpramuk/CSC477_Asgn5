# Assignment 5: NBA Warriors Shot Data

**Data Set:** Warriors 2015-2016 Regular Season NBA Shot Data via the nba_api.

**Analysis Questions:**  
Where did the team primarily shoot from?  
What areas were their shots more likely to go in?  
Best/worst zones?

**Visual Concept:**  
One half of a basketball court overlayed with points for each of the shots taken, colored by make or miss.

**Interaction Concept:**  
Allow the user to highlight a portion of the court and then display statistics about the highlighted area such as total shots in this area, make percentage, top n most frequent shooters in this area.

**Inspiration:**  
[Peter Beshai Buckets](https://buckets.peterbeshai.com/app/)  
[NBA Visuals Shotmaps](https://nbavisuals.com/shotmap)  
[Todd W. Schneider Ballr Shot Charts](https://toddwschneider.com/posts/ballr-interactive-nba-shot-charts-with-r-and-shiny/)

**Data for the 2015-2016 season shots:**

```js
const shotsData = await FileAttachment("warriors_2016_shots.json").json();
console.log("Data for all of the 7159 2015-2016 season shots below:");
display(shotsData);
```
