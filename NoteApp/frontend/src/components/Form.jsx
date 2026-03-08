import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
	const [userName, setUserName] = useState("");
	const [password, setPassword] = useState("");
	const [loading, setLoading] = useState(false);
	const navigate = useNavigate();
	const name = method === "login" ? "Login" : "Register";

	const handleSubmit = async (e) => {
		e.preventDefault();

		try {
			const res = await api.post(route, { username: userName, password });
			if (method === "login") {
				localStorage.setItem(ACCESS_TOKEN, res.data.access);
				localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
				navigate("/");
				return;
			} else {
				navigate("/login");
				return;
			}
		} catch (error) {
			alert(error);
			return;
		} finally {
			setLoading(false);
		}
	};

	return (
		<form onSubmit={handleSubmit} className="form-container">
			<h1>{name}</h1>
			<input type="text" placeholder="Username" value={userName} onChange={(e) => setUserName(e.target.value)} className="form-input" />
			<input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="form-input" />
			{loading && <LoadingIndicator />}
			<button type="submit" disabled={loading} className="form-button">
				{loading ? "Submitting..." : name}
			</button>
		</form>
	);
}

export default Form;
