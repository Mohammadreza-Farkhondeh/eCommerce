import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function ProductList() {
  // Use state hooks to store the products and the error message
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);

  // Use effect hook to fetch products from API once when component mounts
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/products/");
        setProducts(response.data);
      } catch (err) {
        setError(err.response.data.message);
      }
    };
    fetchProducts();
  }, []);

  return (
    <div className="product-list">
      <h1>Products</h1>
      {error && <p className="error">{error}</p>}
      <div className="cards">
        {products.map((product) => (
          <div className="card" key={product.slug}>
            <img src={product.image} alt={product.name} />
            <h2>{product.name}</h2>
            <p>${product.price}</p>
            <Link to={`/products/${product.slug}`}>View Details</Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductList;