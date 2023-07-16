import { useState } from "react";
import api from "../api";

// a custom hook that returns a function to delete the cart item from the API
const useDeleteCartItem = () => {
  // initialize a state variable to store any errors
  const [error, setError] = useState(null);

  // define a function to delete the cart item
  const deleteCartItem = async (slug) => {
    try {
      // make a DELETE request to /cart/{slug}/
      await api.delete(`/cart/${slug}/`);
      // clear any previous errors
      setError(null);
    } catch (error) {
      // handle any errors
      console.error(error);
      setError(error);
    }
  };

  // return the deleteCartItem function and the error state variable
  return [deleteCartItem, error];
};

export default useDeleteCartItem;