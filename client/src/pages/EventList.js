import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import './EventList.css'; // Import CSS for styling

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Fetch events from backend
    axios.get('/api/events') 
      .then(response => {
        setEvents(response.data);
      })
      .catch(error => {
        console.error("Error fetching events", error);
      });
  }, []);

  return (
    <div className="event-list-container">
      <h2>Upcoming Events</h2>
      <div className="events">
        {events.map((event) => (
          <div key={event._id} className="event-card">
            <img src={event.imageUrl} alt={event.name} className="event-image" />
            <div className="event-details">
              <h3>{event.name}</h3>
              <p>{event.location}</p>
              <p>{new Date(event.date).toLocaleDateString()}</p>
              <Link to={`/event/${event._id}`} className="event-link">See Details</Link>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default EventList;
