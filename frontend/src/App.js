import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginForm from "./pages/login";
import SignupForm from "./pages/signup"
import logout from "./pages/logout";
import ProductsList from "./components/ProductsList"
import ProductDetail from "./components/ProductDetail"
import Cart from "./components/Cart";
import CategoryDropdown  from "./components/CategoryDropdown";

function App() {
return (
    <Router>
        <div className="app">
            <h1>Ecommerce Website</h1>
            <CategoryDropdown />
            <Routes>
                <Route path="/" element={<ProductsList />} />
                <Route path="/products/:slug" element={<ProductDetail />} />
                <Route path="/cart" component={Cart} />
                <Route path="/login" element={<LoginForm />} />
                <Route path="/signup" element={<SignupForm />} />
                <Route path="/logout" element={<logout />}/>
            </Routes>
        </div>
    </Router>
    );
}

export default App;