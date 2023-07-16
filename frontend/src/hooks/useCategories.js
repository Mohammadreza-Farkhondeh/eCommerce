import { useState, useEffect } from "react";
import api from "../api";

// a custom hook that returns a list of categories from the API
const useCategories = () => {
  const [categories, setCategories] = useState([]);

  const fetchCategories = async () => {
    try {
      const response = await api.get("/category/?parent__isnull=True");
      // update the state with the response data
      setCategories(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  // use useEffect to call fetchCategories once when the component mounts
  useEffect(() => {
    fetchCategories();
  }, []);

  return categories;
};

export default useCategories;