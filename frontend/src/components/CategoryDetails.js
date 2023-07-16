import React from "react";
import useCategoryDetails from "../hooks/useCategoryDetails";

// a component that renders the subcategories and products of a given category slug
const CategoryDetails = ({ slug }) => {
  // use the custom hook to get the category details
  const details = useCategoryDetails(slug);

  // return a JSX element that renders the subcategories and products
  return (
    <div>
      <h2>{details.category?.name}</h2>
      <h3>Subcategories</h3>
      <ul>
        {details.subcategories?.map((subcategory) => (
          <li key={subcategory.slug}>{subcategory.name}</li>
        ))}
      </ul>
      <h3>Products</h3>
      <ul>
        {details.products?.map((product) => (
          <li key={product.slug}>{product.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryDetails;