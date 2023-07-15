import { useState } from "react";
import axios from "axios";
import { useNavigate, useLocation } from "react-router-dom";

function SignupForm() {
    // Use state hooks to store the form data and the error message
    const [email, setEmail] = useState("");
    const [error, setError] = useState(null);

    // Use navigate and location hooks to handle navigation and state passing
    const navigate = useNavigate();
    const location = useLocation();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Send a post request to the signup endpoint with the email
            const response = await axios.post("http://127.0.0.1:8000/api/user/", { email });
            // If successful, display a success message and redirect to the login page with the email as a state
            alert(response.data.message);
            navigate("/login", { state: { email } });
        } catch (err) {
            setError(err.response.data.message);
        }
    };

    return (
        <div className="signup-form">
            <h1>Signup</h1>
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
                <button type="submit">Signup</button>
            </form>
        </div>
    );
}

export default SignupForm;