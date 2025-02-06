import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import './CreateEvent.css'; // Import CSS for styling

function CreateEvent() {
  const [name, setName] = useState("");
  const [date, setDate] = useState("");
  const [location, setLocation] = useState("");
  const [image, setImage] = useState(null);
  const navigate = useNavigate();

  const handleImageChange = (e) => {
    setImage(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", name);
    formData.append("date", date);
    formData.append("location", location);
    formData.append("image", image);

    try {
      await axios.post('/api/events', formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      navigate("/");
    } catch (error) {
      console.error("Error creating event", error);
    }
  };

  return (
    <div className="create-event-container">
      <h2>Create Your Event</h2>
      <form onSubmit={handleSubmit} className="create-event-form">
        <div className="form-group">
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Date:</label>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Location:</label>
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Event Image:</label>
          <input type="file" onChange={handleImageChange} />
        </div>
        <button type="submit" className="submit-btn">Create Event</button>
      </form>
    </div>
  );
}

export default CreateEvent;
