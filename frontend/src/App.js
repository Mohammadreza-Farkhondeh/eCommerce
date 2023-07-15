import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginForm from "./pages/login";
import SignupForm from "./pages/signup"
import ProductsList from "./components/ProductsList"
import ProductDetail from "./components/ProductDetail"

function App() {
return (
    <Router>
        <div className="app">
            <h1>My App</h1>
            <Routes>
                <Route path="/products" element={<ProductsList />} />
                <Route path="/products/:slug" element={<ProductDetail />} />
                <Route path="/login" element={<LoginForm />} />
                <Route path="/signup" element={<SignupForm />} />
            </Routes>
        </div>
    </Router>
    );
}

export default App;