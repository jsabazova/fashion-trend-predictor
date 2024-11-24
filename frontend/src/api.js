import axios from 'axios';

const API = axios.create({ baseURL: "http://localhost:5000" });

export const scrapeData = () => API.get('/scrape');
export const analyzeData = (inputFile, outputFile) =>
  API.post('/analyze', { input_file: inputFile, output_file: outputFile });
export const visualizeData = () => API.get('/visualize');
export const trainModel = () => API.get('/train');
