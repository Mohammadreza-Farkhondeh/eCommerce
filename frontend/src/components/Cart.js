import React from "react";
import useCart from "../hooks/useCart";
import useUpdateCartItem from "../hooks/useUpdateCartItem";
import useDeleteCartItem from "../hooks/useDeleteCartItem";

// a component that renders the cart items and total, and handles the user actions
const Cart = () => {
  // use the custom hooks to get the cart data and functions
  const { items, total } = useCart();
  const updateCartItem = useUpdateCartItem();
  const deleteCartItem = useDeleteCartItem();

  // define a function to handle the click event of the increase button
  const handleIncrease = (slug, quantity) => {
    // update the cart item quantity in the API with one more unit
    updateCartItem(slug, quantity + 1);
  };

  // define a function to handle the click event of the decrease button
  const handleDecrease = (slug, quantity) => {
    // check if the quantity is more than one
    if (quantity > 1) {
      // update the cart item quantity in the API with one less unit
      updateCartItem(slug, quantity - 1);
    } else {
      // delete the cart item from the API
      deleteCartItem(slug);
    }
  };

  // define a function to handle the click event of the remove button
  const handleRemove = (slug) => {
    // delete the cart item from the API
    deleteCartItem(slug);
  };

  // return a JSX element that renders the cart items and total
  return (
    <div>
      <h2>Cart</h2>
      <ul>
        {items && items.map((item) => (
          <li key={item.product.slug}>
            {item.product.name} - ${item.product.price} x {item.quantity} = $
            {item.subtotal}
            <button onClick={() => handleIncrease(item.product.slug, item.quantity)}>
              +
            </button>
            <button onClick={() => handleDecrease(item.product.slug, item.quantity)}>
              -
            </button>
            <button onClick={() => handleRemove(item.product.slug)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
      <p>Total: ${total}</p>
    </div>
  );
};

export default Cart;