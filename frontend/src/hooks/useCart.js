import { useState, useEffect } from "react";
import api from "../api";

// a custom hook that returns an object with cart items and total from the API
const useCart = () => {
  const [cart, setCart] = useState({});

  const fetchCart = async () => {
    try {
      const response = await api.get("/cart/");
      // update the state with the response data
      setCart(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  // use useEffect to call fetchCart once when the component mounts
  useEffect(() => {
    fetchCart();
  }, []);

  return cart;
};

export default useCart;