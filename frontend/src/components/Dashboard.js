import React, { useState } from "react";
import { scrapeData, analyzeData, visualizeData, trainModel } from "../api";

const Dashboard = () => {
  const [message, setMessage] = useState("");

  const handleScrape = async () => {
    const res = await scrapeData();
    setMessage(res.data.message);
  };

  const handleAnalyze = async () => {
    const res = await analyzeData();
    setMessage(res.data.message);
  };

  const handleVisualize = async () => {
    const res = await visualizeData();
    setMessage(res.data.message);
  };

  const handleTrain = async () => {
    const res = await trainModel();
    setMessage(res.data.message);
  };

  return (
    <div>
      <h1>Fashion Trend Predictor</h1>
      <button onClick={handleScrape}>Scrape Data</button>
      <button onClick={handleAnalyze}>Analyze Data</button>
      <button onClick={handleVisualize}>Visualize Data</button>
      <button onClick={handleTrain}>Train Model</button>
      <p>{message}</p>
    </div>
  );
};

export default Dashboard;
