## Introduction

This is a javascript library to easily build interactive graphs in a circular layout. It's based on [d3.js](https://d3js.org/). It aims to be a javascript version of the [Circos](http://circos.ca) software.

## Tracks

A track is a series of data points.

To add a track to your graph you should write something like this:

```javascript
myCircos.heatmap(
    'my-heatmap',
    data,
    {
        // your heatmap configuration (optional)
    },
);
```

This pattern is similar to all track types:

```javascript
myCircos.trackType('track-id', data, configuration);
```

**Note**: The track name is used as a HTML class name so here are the format limitations.

* Must be unique.
* Should be slug style for simplicity, consistency and compatibility. Example: `my-heatmap`
* Lowercase, a-z, can contain digits, 0-9, can contain dash or dot but not start/end with them.
* Consecutive dashes or dots not allowed.
* 50 characters or less.


### Chords

Chords tracks connect layout regions.

<p align="center">
  <img src="doc/chords.png" width="60%" alt="chords">
  <br/>
  <i>Some gene fusions in human karyotype (<a href="demo/chords.js">source</a>)</i>
</p>

Data should looks like this:

```javascript
var data = [
  {
    source: {
      id: 'january',
      start: 1,
      end: 12
    },
    target: {
      id: 'april',
      start: 18,
      end: 20
    }
  },
  {
    source: {
      id: 'february',
      start: 20,
      end: 28
    },
    target: {
      id: 'december',
      start: 1,
      end: 13
    }
  },
  ...
];
```

Optionally each datum can define a `value` attribute to draw colored ribbons with palettes or a color function.

The available configuration fields are:
- [color](#color)
- [events](#events)
- [opacity](#opacity)
- [zIndex](#zIndex)
- [tooltipContent](#tooltipContent)
- [min](#minmax)
- [max](#minmax)
- [radius](#radius)
- [logScale](#logScale)
- [logScaleBase](#logScaleBase)

### Heatmap

<p align="center">
  <img src="doc/heatmap.png" width="60%" alt="heatmap">
  <br/>
  <i>Electrical comsumption in France in 2014</i>
</p>

To add a heatmap to your circos instance:

```javascript
myCircos.heatmap('electrical-consumption', data, configuration);
```

Configuration:

```javascript
{
  innerRadius: null,
  outerRadius: null,
  min: null,
  max: null,
  color: 'YlGnBu',
  logScale: false,
  tooltipContent: null,
  events: {}
}
```

Data format:

```javascript
var data = [
  {
    block_id: 'january',
    start: 0,
    end: 1,
    value: 1368001
  },
  {
    block_id: 'january',
    start: 1,
    end: 2,
    value: 1458583
  },
  ...
]
```

### Highlight

To add a highlight to your circos instance:

```javascript
myCircos.highlight('cytobands', data, configuration);
```

The minimal datum should have `block_id`, `start` and `end` attributes.

Configuration:

```javascript
{
  innerRadius: null,
  outerRadius: null,
  min: null,
  max: null,
  color: 'd3d3d3',
  strokeColor: null,
  strokeWidth: 0,
  opacity: 1,
  logScale: false,
  tooltipContent: null,
  events: {}
}
```

### Histogram
Data should looks like this:

```javascript
var data = [
    {
      block_id: 'january',
      start: 1,
      end: 10,
      value: 5
    }
];
```

The available configuration fields are:
- [innerRadius](#innerRadiusOuterRadius)
- [outerRadius](#innerRadiusOuterRadius)
- [color](#color)
- [opacity](#opacity)
- [zIndex](#zIndex)
- [tooltipContent](#tooltipContent)
- [min](#minmax)
- [max](#minmax)
- [logScale](#logScale)
- [logScaleBase](#logScaleBase)
- [axes](#axes)
- [events](#events)

### Line

<p align="center">
  <img src="doc/line.png" width="60%" alt="line">
  <br/>
  <i>Some single nucleotide polymorphism on chromosomes 1, 2 and 3 (<a href="demo/line.js">source</a>)</i>
</p>

```javascript
myCircos.line('line1', data, configuration);
```

The minimal datum should have `block_id`, `position` and `value` attributes (see above tracks for more details).

The available configuration fields are:
- [innerRadius](#innerRadiusOuterRadius)
- [outerRadius](#innerRadiusOuterRadius)
- [color](#color)
- [strokeColor](#strokeColor)
- [strokeWidth](#strokeWidth)
- [direction](#direction)
- [fill](#fill)
- [fillColor](#fillColor)
- [maxGap](#maxGap)
- [opacity](#opacity)
- [zIndex](#zIndex)
- [min](#minmax)
- [max](#minmax)
- [logScale](#logScale)
- [logScaleBase](#logScaleBase)
- [axes](#axes)
- [backgrounds](#backgrounds)
- [events](#events)

**Note**: The tooltip option is not available for line track. To display a tooltip, you should superimpose an invisble `scatter` track (`fill: false` and `strokeWidth: 0`) and set a tooltip for this track.

### Scatter
```javascript
myCircos.scatter('scatter1', data, configuration);
```

The minimal datum should have `block_id`, `position` and `value` attributes (see above tracks for more details).

The available configuration fields are:
- [innerRadius](#innerRadiusOuterRadius)
- [outerRadius](#innerRadiusOuterRadius)
- [color](#color)
- [strokeColor](#strokeColor)
- [strokeWidth](#strokeWidth)
- [direction](#direction)
- [fill](#fill)
- [size](#size)
- [shape](#shape)
- [opacity](#opacity)
- [zIndex](#zIndex)
- [min](#minmax)
- [max](#minmax)
- [logScale](#logScale)
- [logScaleBase](#logScaleBase)
- [axes](#axes)
- [backgrounds](#backgrounds)
- [events](#events)

### Stack
```javascript
myCircos.stack('stack', data, configuration);
```

The minimal datum should have `block_id`, `start` and `end` attributes (see above tracks for more details).

Configuration:

```javascript
{
  innerRadius: null,
  outerRadius: null,
  min: null,
  max: null,
  color: '#fd6a62',
  strokeColor: '#d3d3d3',
  strokeWidth: 1,
  direction: 'out',
  thickness: 10,
  radialMargin: 2,
  margin: 2,
  opacity: 1,
  logScale: false,
  tooltipContent: null,
  events: {}
}
```

### Text
```javascript
myCircos.text('text', data, configuration);
```

The minimal datum should have `block_id`, `position` and `value` attributes (see above tracks for more details).

Configuration:

```javascript
{
  innerRadius: null,
  outerRadius: null,
  style: {
    'font-size': 12,
    fill: 'black',
    opacity: 1,
  },
  events: {}
}
```

## Configuration Attributes

### backgrounds

You can add a list of backgrounds:

```javascript
{
  backgrounds: [
    {
      start: 0.006,
      color: '#4caf50',
      opacity: 0.1
    },
    {
      start: 0.002,
      end: 0.006,
      color: '#d3d3d3',
      opacity: 0.1
    },
    {
      end: 0.002,
      color: '#f44336',
      opacity: 0.1
    }
  ]
}
```

The `start` and `end` fields are interpreted as values on the same scale than the track values.
- If `start` is not specified, default is the `min` value of the track.
- If `end` is not specified, default is the `max` value of the track.

You can also specify a `color` and an `opacity`.

### events

All tracks and the layout configurations can receive an events attribute. This attribute must be an object where keys are event names and values are event callbacks. For example:

```javascript
{
  events: {
    'click.alert': function (datum, index, nodes, event) {
      window.alert(datum)
    }
  }
}
```

The documentation about d3 events is [here](https://github.com/d3/d3-selection/blob/master/README.md#selection_on). You can add all events described in this documentation. I recommend using event namespaces (`click.alert` instead of `click`) to avoid possible conflicts with internal circosjs events.

### innerRadius/outerRadius

For the layout, the innerRadius and outerRadius values are always interpreted as a number of pixel.

For tracks:

If innerRadius and outerRadius are between `0` and `1`, the value is interpreted as a fraction of the innerRadius of the layout.

eg:
```
{
  innerRadius: 0.5,
  outerRadius: 0.8
}
```

If innerRadius and outerRadius are between `1` and `10`, the value is interpreted as a fraction of the outerRadius of the layout.

eg:
```
{
  innerRadius: 1,
  outerRadius: 1.2
}
```

Otherwise it is interpreted as a number of pixels.

### min/max

The default min and max values are computed according to the dataset. You can override these values by specifying a `min` or `max` attribute in the configuration.

### color

The color attribute can be either:

#### CSS color code

e.g `#d3d3d3`, `blue`, `rgb(0, 0, 0)`

#### Palette name from [d3-scale-chromatic](https://github.com/d3/d3-scale-chromatic)

The color will be computed dynamically according to the track data `value` field.

If you prefix the palette name with a `-` (e.g `-BrBG`), the palette will be reversed.

The list of palette names are:

**BrBG**:
<img src="doc/palettes/BrBG.png" width="100%" height="10">
**PRGn**:
<img src="doc/palettes/PRGn.png" width="100%" height="10">
**PiYG**:
<img src="doc/palettes/PiYG.png" width="100%" height="10">
**PuOr**:
<img src="doc/palettes/PuOr.png" width="100%" height="10">
**RdBu**:
<img src="doc/palettes/RdBu.png" width="100%" height="10">
**RdGy**:
<img src="doc/palettes/RdGy.png" width="100%" height="10">
**RdYlBu**:
<img src="doc/palettes/RdYlBu.png" width="100%" height="10">
**RdYlGn**:
<img src="doc/palettes/RdYlGn.png" width="100%" height="10">
**Spectral**:
<img src="doc/palettes/Spectral.png" width="100%" height="10">
**Blues**:
<img src="doc/palettes/Blues.png" width="100%" height="10">
**Greens**:
<img src="doc/palettes/Greens.png" width="100%" height="10">
**Greys**:
<img src="doc/palettes/Greys.png" width="100%" height="10">
**Oranges**:
<img src="doc/palettes/Oranges.png" width="100%" height="10">
**Purples**:
<img src="doc/palettes/Purples.png" width="100%" height="10">
**Reds**:
<img src="doc/palettes/Reds.png" width="100%" height="10">
**BuGn**:
<img src="doc/palettes/BuGn.png" width="100%" height="10">
**BuPu**:
<img src="doc/palettes/BuPu.png" width="100%" height="10">
**GnBu**:
<img src="doc/palettes/GnBu.png" width="100%" height="10">
**OrRd**:
<img src="doc/palettes/OrRd.png" width="100%" height="10">
**PuBuGn**:
<img src="doc/palettes/PuBuGn.png" width="100%" height="10">
**PuBu**:
<img src="doc/palettes/PuBu.png" width="100%" height="10">
**PuRd**:
<img src="doc/palettes/PuRd.png" width="100%" height="10">
**RdPu**:
<img src="doc/palettes/RdPu.png" width="100%" height="10">
**YlGnBu**:
<img src="doc/palettes/YlGnBu.png" width="100%" height="10">
**YlGn**:
<img src="doc/palettes/YlGn.png" width="100%" height="10">
**YlOrBr**:
<img src="doc/palettes/YlOrBr.png" width="100%" height="10">
**YlOrRd**:
<img src="doc/palettes/YlOrRd.png" width="100%" height="10">

#### Custom function

You can specify a function that compute the color code given the track data and the datum index. For example:

```javascript
{
  color: function(datum, index) {
    return datum.value < 5 ? 'red' : 'green'
  }
}

```

### axes

The default value is an empty array:

```javascript
{
  axes: []
}
```

You can add items to this array to render an axis or a group of axes. You can give axes a `color` (default: '#d3d3d3'), `thickness` (default: 1) and `opacity` (default: track opacity):

```javascript
{
  axes: [
    {
      color: 'black',
      thickness: 2, // in pixel
      opacity: 0.3 // between 0 and 1
    }
  ]
}
```

Then you should specify where to place the axes.

You can either define a single axis by defining a `position` attribute with a value between the min and max value of the track:

```javascript
{
  axes: [
    {
      color: 'red',
      position: 4
    },
    {
      color: 'green',
      position: 15
    }
  ]
}
```

<p align="center">
  <img src="doc/axes-1.png" width="60%" alt="axes-1">
  <br/>
  <i><a href="demo/axes">source</a></i>
</p>


Or define a range of axes with a `spacing` attribute and optionnally a `start` and `end` attributes:

```javascript
{
  axes: [
    {
      spacing: 2
    }
  ]
}
```

<p align="center">
  <img src="doc/axes-2.png" width="60%" alt="axes-2">
  <br/>
  <i><a href="demo/axes">source</a></i>
</p>

Here is an advanced example:

```javascript
{
  axes: [
    {
      color: 'red',
      spacing: 2,
      end: 4
    },
    {
      color: 'green',
      spacing: 2,
      start: 16
    },
    {
      spacing: 2,
      start: 4,
      end: 16,
      thickness: 2
    },
    {
      spacing: 1,
      start: 4,
      end: 16,
      thickness: 1
    }
  ]
}
```

<p align="center">
  <img src="doc/axes-3.png" width="60%" alt="axes-3">
  <br/>
  <i><a href="demo/axes">source</a></i>
</p>

The values that you set for `position`, `spacing`, `start` and `end` are in the unit of the track values.

### tooltipContent

A function that receive the datum and the index as a value and return a string displayed in the tooltip (HTML is accepted):

```javascript
{
  tooltipContent: function (datum, index) {
    return `<h5>${datum.block_id}:${datum.start}-${datum.end} ➤ ${datum.value}</h5> <i>(CTRL+C to copy to clipboard)</i>`
  }
}
```

Then when you mouseover the datum, a tooltip will be displayed.
Note that you can use the keyboard shortcut CTRL+C to copy the content to clipboard.

### showAxesTooltip

Show or not a tooltip with the value of the axis. Default is `true`.

### direction

It should be either `in` or `out`. Default is `out`. For stack you can also use `center`.

### fill

`true` or `false`.

### fillColor

A color such as `#d3d3d3`, `red`, `rgb(112, 255, 1)`.

### logScale

`true` or `false`. Default is `false`.

### logScaleBase

The log base if logScale is `true`. Default is `Math.E`.

### radius

In the chords configuration you can specify a radius parameter. Default is `null`.

Examples:

```javascript
// when there is no value, default is null:
// the radius will be the one of the innerRadius of the layout
{}

// when the value is a number greater than 1, it is interpreted as
// a number of pixel from the center
{
  radius: 200
}

// when the value is a number lower than 1, it is interpreted as
// a fraction of the layout inner radius
{
  radius: 0.8
}

// you can also specify a function that return a number that
// will be interpreted as explained above. The function takes
// a datum as parameter
{
  radius: function (d) {
    if (d.source.id === 'chr1') {
      return 0.8
    }
    if (d.source.id === 'chr2') {
      return 0.7
    }
  }
}
```

### shape

It should be one of:
  - `circle`
  - `cross`
  - `diamond`
  - `square`
  - `triangle`
  - `star`
  - `wye`

### zIndex

This should be an integer. The higher it is the more above the track will appear.


----
---

Above is the usage documentation for this function library.  
Next, I will guide you on how to load data, process it, and use it to generate charts. Below are the detailed steps.

1. **Loading Data**  
You can load data from a specified path using the `readFile` function. This is commonly used to load CSV or JSON files. The loaded data will be used for subsequent chart generation.  
For example:  
```js
let level2 = await readFile('id_001/file2.csv'); 
```

2. **Processing Data**  
After loading the data, some preprocessing is needed according to the requirements of the target chart.  
For instance, you may need to aggregate data by chromosome intervals, filter based on certain conditions, or transform data formats. These operations are performed by the following utility functions:  
- **Aggregate Data**  
  - When creating Heatmap, Highlight, or Histogram charts, you need to use `reduceData` and `reduceData_Position` to aggregate data based on chromosome or position intervals.  
- **Transform Data**  
   If the file contains columns named `Start` and `End`, but the chart requires `Position`, you need to use `transform_startend_position`. This function automatically converts `Start` and `End` to `Position` and returns the new data.

3. **Generate Charts**  
Charts are generated using the format `circos.{chartType}('track-id', data, configuration)`.  
The `track-id` is defined by you, but it must be a unique value.

---

### Below is a detailed explanation of the utility functions for data processing:

# Function Documentation

This document describes in detail the functionality, parameters, and return values of three functions. These functions are primarily used for processing genomic data, performing data aggregation, and conversion operations. The details are as follows:

---

## 1. `reduceData`
### What type of chart will use this function?
- Histogram
- Heatmap

### Functionality  
This function divides the data based on the chromosome information and counts the number of data points in each interval. It is suitable for data represented by `Start` and `End` positions.

### Parameters  

- **rawData**  
  - **Type**: Array  
  - **Description**: The genomic data array, where each object contains the following fields:  
    - `id`: Chromosome ID (string).  
    - `Start`: Starting position (number).  
    - `End`: Ending position (number).  

- **karyotype**  
  - **Type**: Array  
  - **Description**: The chromosome information array, where each object contains the following fields:  
    - `id`: Chromosome ID (string).  
    - `len`: Chromosome length (number).  

- **range**  
  - **Type**: Number (optional)  
  - **Description**: Interval length, default is `10,000,000`.  

### Return Value  
- **Type**: Array  
- **Description**: The aggregated result array, where each object contains the following fields:  
  - `block_id`: Chromosome ID.  
  - `start`: Interval start position.  
  - `end`: Interval end position.  
  - `value`: The number of data points in the interval.

### Example Code  
```js
const result = reduceData(rawData, karyotype, 5000000);
```

---

## 2. `reduceData_Position`
### What type of chart will use this function?
- Histogram
- Heatmap

### Functionality  
This function is similar to `reduceData`, but the input data uses a single `Position` field instead of `Start` and `End`. This function is suitable for data that only includes `Position`.

### Parameters  

- **rawData**  
  - **Type**: Array  
  - **Description**: The genomic data array, where each object contains the following fields:  
    - `id`: Chromosome ID (string).  
    - `Position`: Position of the data (number).  

- **karyotype**  
  - **Type**: Array  
  - **Description**: The chromosome information array, where each object contains the following fields:  
    - `id`: Chromosome ID (string).  
    - `len`: Chromosome length (number).  

- **range**  
  - **Type**: Number (optional)  
  - **Description**: Interval length, default is `10,000,000`.  

### Return Value  
- **Type**: Array  
- **Description**: The aggregated result array, where each object contains the following fields:  
  - `block_id`: Chromosome ID.  
  - `start`: Interval start position.  
  - `end`: Interval end position.  
  - `value`: The number of data points in the interval.

### Example Code  
```js
const result = reduceData_Position(rawData, karyotype, 5000000);
```

---

## 3. `transform_startend_position`
### What type of chart will use this function?
- Line
- Scatter

### Functionality  
This function converts the `Start` and `End` positions in the input genomic data into the corresponding `Position`, generating data entries for each position. It is used for converting interval data into specific position data.

### Parameters  

- **inputData**  
  - **Type**: Array (JSON format)  
  - **Description**: The genomic data array containing `id`, `Start`, and `End` fields.  

- **number_column**  
  - **Type**: String (optional)  
  - **Description**: Specifies the column name to be converted into the `value` field. If this parameter is provided, the values from this column will be parsed as floating-point numbers; otherwise, `value` will default to 1.  

### Return Value  
- **Type**: Array  
- **Description**: The transformed data array, where each object contains the following fields:  
  - `block_id`: Chromosome ID.  
  - `position`: Converted position (from `Start` or `End`).  
  - `value`: The corresponding data value at that position (if `number_column` is provided, it uses that column’s value; otherwise, it defaults to 1).

### Example Code  
```js
const result = transform_startend_position(inputData, "ValueColumn");
```

---
