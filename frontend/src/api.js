import axios from "axios";

// create an axios instance with the base URL of your Django API
const api = axios.create({
  baseURL: "http://localhost:8000/",
});

export default api;