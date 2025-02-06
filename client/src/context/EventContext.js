import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

export const EventContext = createContext();

export const EventProvider = ({ children }) => {
  const [events, setEvents] = useState([]);

  const fetchEvents = async () => {
    try {
      const res = await axios.get("http://localhost:5000/api/events");
      setEvents(res.data);
    } catch (err) {
      console.error("Error fetching events:", err);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  return (
    <EventContext.Provider value={{ events, fetchEvents }}>
      {children}
    </EventContext.Provider>
  );
};
