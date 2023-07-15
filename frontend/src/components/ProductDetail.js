import { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

function ProductDetail() {
  // Use state hooks to store the product and the error message
  const [product, setProduct] = useState(null);
  const [error, setError] = useState(null);

  // Use params hook to get the product slug from the URL
  const { slug } = useParams();

  // Use effect hook to fetch product from API once when component mounts or slug changes
  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(`/api/products/${slug}`);
        setProduct(response.data);
      } catch (err) {
        setError(err.response.data.message);
      }
    };
    fetchProduct();
  }, [slug]);

  return (
    <div className="product-detail">
      <h1>Product Detail</h1>
      {error && <p className="error">{error}</p>}
      {product && (
        <>
          <img src={product.image} alt={product.name} />
          <h2>{product.name}</h2>
          <p>${product.price}</p>
          <p>{product.description}</p>
          {/* TODO: Add a button or a link to add product to cart */}
        </>
      )}
    </div>
  );
}

export default ProductDetail;