import React, { useState } from "react";
import useCategories from "../hooks/useCategories";

// a component that renders a dropdown menu of categories
const CategoryDropdown = ({ onSelect }) => {
  // use the custom hook to get the categories
  const categories = useCategories();

  const [selected, setSelected] = useState("");

  const handleChange = (event) => {
    // get the value of the selected option
    const value = event.target.value;
    // update the state with the value
    setSelected(value);
    // call the onSelect prop function with the value
    onSelect(value);
  };

  return (
    <select value={selected} onChange={handleChange}>
      <option value="">Select a category</option>
      {categories.map((category) => (
        <option key={category.slug} value={category.slug}>
          {category.name}
        </option>
      ))}
    </select>
  );
};

export default CategoryDropdown;