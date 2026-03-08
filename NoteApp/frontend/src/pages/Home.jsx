import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note";
import "../styles/Home.css";

function Home() {
	const [notes, setNotes] = useState([]);
	const [content, setContent] = useState("");
	const [title, setTitle] = useState("");

	const getNote = async () => {
		api.get("/api/notes/")
			.then((res) => res.data)
			.then((data) => {
				setNotes(data);
				console.log(data);
			})
			.catch((err) => alert(err));
	};

	const deleteNote = async (id) => {
		api.delete(`/api/notes/${id}/`)
			.then((res) => {
				if (res.status === 204) {
					alert("Note deleted successfully");
				} else {
					alert("Failed to delete note");
				}
				getNote();
			})
			.catch((err) => alert(err));

		getNote();
	};

	const createNote = async (e) => {
		e.preventDefault();
		api.post("/api/notes/", { title, content })
			.then((res) => {
				if (res.status === 201) {
					alert("Note created successfully");
				}
			})
			.catch((err) => alert(err));
		getNote();
	};

	useEffect(() => {
		getNote();
	}, []);

	return (
		<div>
			<div>
				<h1>Notes</h1>
				{notes.map((note) => (
					<Note key={note.id} note={note} onDelete={deleteNote} />
				))}
			</div>
			<h2>Create a New Note</h2>
			<form onSubmit={createNote}>
				<label>Title:</label>
				<br />
				<input type="text" placeholder="Title" name="title" value={title} onChange={(e) => setTitle(e.target.value)} />
				<textarea placeholder="Content" name="content" value={content} onChange={(e) => setContent(e.target.value)} />
				<button type="submit">Create Note</button>
			</form>
		</div>
	);
}

export default Home;
