import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignupForm from "./pages/signup"

function App() {
  return (
    <Router>
      <div className="app">
        <h1>My App</h1>
        <Routes>
          <Route path="/signup" element={<SignupForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;