import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    size_sqm: 120,
    bedrooms: 2,
    location: 'City Center'
  });
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);

  const locations = ['Downtown', 'Suburban', 'Rural', 'City Center', 'Industrial'];

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPrice(null);

    try {
      // Connect to your Python Backend on Port 8001
      const response = await fetch('http://127.0.0.1:8001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setPrice(data.predicted_price);
    } catch (error) {
      console.error("Error connecting to AI:", error);
      alert("Could not connect to the AI Backend. Is it running on Port 8001?");
    }
    setLoading(false);
  };

  return (
    <div className="App" style={{ padding: "50px", fontFamily: "Arial", backgroundColor: "#f0f2f5", height: "100vh" }}>
      <h1 style={{ textAlign: 'center', color: '#333' }}>🏡 AI Real Estate Validator</h1>
      <div style={{ maxWidth: "400px", margin: "0 auto", backgroundColor: "white", padding: "30px", borderRadius: "15px", boxShadow: "0 4px 8px rgba(0,0,0,0.1)" }}>
        <form onSubmit={handleSubmit}>
          
          <div style={{ marginBottom: "20px" }}>
            <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>Size (sqm): </label>
            <input 
              type="number" 
              name="size_sqm" 
              value={formData.size_sqm} 
              onChange={handleChange} 
              style={{ width: "100%", padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }}
            />
          </div>

          <div style={{ marginBottom: "20px" }}>
            <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>Bedrooms: </label>
            <input 
              type="number" 
              name="bedrooms" 
              value={formData.bedrooms} 
              onChange={handleChange} 
              style={{ width: "100%", padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }}
            />
          </div>

          <div style={{ marginBottom: "20px" }}>
            <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold" }}>Location: </label>
            <select 
              name="location" 
              value={formData.location} 
              onChange={handleChange}
              style={{ width: "100%", padding: "10px", borderRadius: "5px", border: "1px solid #ddd" }}
            >
              {locations.map(loc => <option key={loc} value={loc}>{loc}</option>)}
            </select>
          </div>

          <button 
            type="submit" 
            style={{ 
              width: "100%", 
              padding: "12px", 
              backgroundColor: "#007bff", 
              color: "white", 
              border: "none", 
              borderRadius: "5px",
              cursor: "pointer",
              fontSize: "16px",
              fontWeight: "bold"
            }}
          >
            {loading ? "Calculating..." : "Predict Price"}
          </button>

        </form>

        {price && (
          <div style={{ marginTop: "20px", padding: "15px", backgroundColor: "#d4edda", color: "#155724", borderRadius: "5px", textAlign: "center" }}>
            <h3 style={{ margin: "0 0 10px 0" }}>Estimated Value:</h3>
            <h2 style={{ margin: 0, fontSize: "28px" }}>${price.toLocaleString()}</h2>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;