import { useState, useEffect } from "react";
import api from "../api";

// a custom hook that returns an object with subcategories and products of a given category slug
const useCategoryDetails = (slug) => {
  const [details, setDetails] = useState({});

  const fetchCategoryDetails = async () => {
    try {
      const response = await api.get("/category/${slug}/");
      // update the state with the response data
      setDetails(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  // use useEffect to call fetchCategoryDetails whenever slug changes
  useEffect(() => {
    if (slug) {
      fetchCategoryDetails();
    }
  }, [slug]);

  return details;
};

export default useCategoryDetails;