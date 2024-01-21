import React, { useState } from "react";
import { AgChartsReact } from "ag-charts-react";

export const TrackScatterChart = (props) => {
  const { title = "", tracks = [] } = props;
  const [options, setOptions] = useState({
    title: {
      text: title,
    },
    series: [
      {
        type: "scatter",
        xKey: "index",
        xName: "Title Of Song",
        yKey: "danceability",
        yName: "Danceablity of song",
        data: tracks,
      },
    ],
    axes: [
      {
        type: "number",
        position: "bottom",
        title: {
          text: "Index of song",
        },
      },
      {
        type: "number",
        position: "left",
        title: {
          text: "Danceablity of song",
        },
      },
    ],
  });
  return <AgChartsReact options={options} />;
};

export const TrackHistogram = (props) => {
  const { title = "", tracks = [] } = props;
  const [options, setOptions] = useState({
    title: {
      text: title,
    },
    data: tracks,
    series: [
      {
        type: "histogram",
        xKey: "duration_seconds",
        xName: "Song Duration",
      },
    ],
    axes: [
      {
        type: "number",
        position: "bottom",
        title: { text: "Song Duration" },
      },
      {
        type: "number",
        position: "left",
        title: { text: "Index of song" },
      },
    ],
  });
  return <AgChartsReact options={options} />;
};

export const TrackBarChart = (props) => {
  const { title = "", tracks = [] } = props;
  const [options, setOptions] = useState({
    title: {
      text: title,
    },
    data: tracks,
    series: [
      {
        type: "bar",
        xKey: "acousticness",
        yKey: "index",
        yName: "Acousticness",
      },
      {
        type: "bar",
        xKey: "tempo",
        yKey: "index",
        yName: "tempo",
      },
    ],
  });
  return <AgChartsReact options={options} />;
};
