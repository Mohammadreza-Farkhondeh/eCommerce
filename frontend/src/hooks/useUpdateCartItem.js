import { useState } from "react";
import api from "../api";

// a custom hook that returns a function to update the cart item quantity in the API
const useUpdateCartItem = () => {
  // initialize a state variable to store any errors
  const [error, setError] = useState(null);

  // define a function to update the cart item quantity
  const updateCartItem = async (slug, quantity) => {
    try {
      // make a PATCH request to /cart/{slug}/ with the quantity data
      await api.patch("/api/cart/${slug}/", { quantity });
      // clear any previous errors
      setError(null);
    } catch (error) {
      // handle any errors
      console.error(error);
      setError(error);
    }
  };

  // return the updateCartItem function and the error state variable
  return [updateCartItem, error];
};

export default useUpdateCartItem;