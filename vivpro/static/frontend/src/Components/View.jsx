import React, { useState, useEffect } from "react";
import { getMusicTracks } from "../services";

import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";

import { AgGridReact } from "ag-grid-react";
import "ag-grid-community/styles/ag-grid.css"; // Core CSS
import "ag-grid-community/styles/ag-theme-quartz.css"; // Theme

import { Rating } from "./Rating";
import { TrackBarChart, TrackHistogram, TrackScatterChart } from "./TrackCharts";

export const View = () => {
  const [tracks, setTracks] = useState([]);
  const [colDefs, setColDefs] = useState([
    { field: "id" },
    { field: "title", filter: true },
    { field: "rating", cellRenderer: Rating },
  ]);

  useEffect(() => {
    const initTracks = async () => {
      const tracks = await getMusicTracks();
      setTracks(tracks?.instances || []);
    };
    initTracks();
  }, []);

  return (
    <Tabs
      defaultActiveKey="table"
      id="uncontrolled-tab-example"
      className="m-2"
    >
      <Tab eventKey="table" title="Table">
        {!!tracks.length && (
          <>
            <div className="grid-title"> Track List </div>
            <div className="ag-theme-quartz table-styles">
              <AgGridReact
                rowData={tracks}
                pagination={true}
                columnDefs={colDefs}
                paginationPageSize={10}
                paginationPageSizeSelector={false}
                onGridReady={(params) => params.api.sizeColumnsToFit()}
              />
            </div>
          </>
        )}
      </Tab>
      <Tab eventKey="charts" title="Charts">
        {!!tracks.length && (
          <div className="m-4">
            <TrackScatterChart
              title="Danceability Scatter Chart"
              tracks={tracks}
            />
            <TrackHistogram
              title="Song Duration Chart"
              tracks={tracks}
            />
            <TrackBarChart title="Song Acousticness and Tempo Chart"
              tracks={tracks}/>
          </div>
        )}
      </Tab>
    </Tabs>
  );
};
