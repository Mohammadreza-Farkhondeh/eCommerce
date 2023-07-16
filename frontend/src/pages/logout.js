import axios from "axios";
import { useHistory } from "react-router-dom";
import Cookies from "js-cookie";
// import api from "../api";

function LogoutButton() {
    // Use history hook to navigate to other pages
    const history = useHistory();

    // Handle the logout button click
    const handleLogout = async () => {
    try {
        // Get the refresh token from the cookies
        const refreshToken = Cookies.get("refresh");
        // Send a post request to the logout endpoint with the refresh token

        // TODO: implement logout view in backend
        //await api.post("/api/user/logout/", { refresh });


        // If successful, remove the tokens from the cookies and clear the authorization header
        Cookies.remove("access");
        Cookies.remove("refresh");
        delete axios.defaults.headers.common["Authorization"];
        // Redirect to the login page
        history.push("/login");
    } catch (err) {
        // If error, display an alert message
        alert(err.response.data.message);
    }
    };

    return (
        <div className="logout-button">
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
    }

export default LogoutButton;