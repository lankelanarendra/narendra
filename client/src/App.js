import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import { EventProvider } from "./context/EventContext";
import CreateEvent from "./pages/CreateEvent";
import EventList from "./pages/EventList";

function App() {
  return (
    <EventProvider>
      <Router>
        <div className="app-container">
          <header className="app-header">
            <h1>Event Management Platform</h1>
            <nav>
              <Link to="/">Events</Link> | <Link to="/create">Create Event</Link>
            </nav>
          </header>
          <Routes>
            <Route path="/" element={<EventList />} />
            <Route path="/create" element={<CreateEvent />} />
          </Routes>
        </div>
      </Router>
    </EventProvider>
  );
}

export default App;
