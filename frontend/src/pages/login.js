import { useState } from "react";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";
import Cookies from "js-cookie";

function LoginForm() {
    // Use location hook to get the email from the state
    const location = useLocation();
    const emailFromState = location.state?.email;

    // Use state hooks to store the form data and the error message
    const [email, setEmail] = useState(emailFromState || "");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);

    // Use Navigate hook to navigate to other pages
    const navigate = useNavigate();

    // Handle the form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Send a post request to the login endpoint with the email and password
            const response = await axios.post("http://127.0.0.1:8000/api/user/token/", { email, password });
            // If successful, store the token pair in cookies and set the authorization header for future requests
            Cookies.set("access", response.data.access);
            Cookies.set("refresh", response.data.refresh);
            axios.defaults.headers.common["Authorization"] =
                "Bearer " + response.data.access;
            // Redirect to the home page
            navigate("/");
        } catch (err) {
            // If error, set the error state to display the message
            setError(err.response.data.message);
        }
    };

    return (
        <div className="login-form">
            <h1>Login</h1>
            {error && <p className="error">{error}</p>}
            <form onSubmit={handleSubmit}>
                <label htmlFor="email">Email</label>
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default LoginForm;