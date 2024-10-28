import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Ensure you import the CSS file

function App() {
  const [image, setImage] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handle image selection
  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  // Handle form submission to send the image
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) {
      setError("Please select an image first");
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', image);

    try {
      const res = await axios.post('http://127.0.0.1:5000/predict', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Assuming the response is a JSON object
      setResponse(res.data);
    } catch (err) {
      setError("Error uploading the image or receiving response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h2>Upload Image for Prediction</h2>

      <form onSubmit={handleSubmit} className="form-container">
        <input 
          type="file" 
          accept="image/*" 
          onChange={handleImageChange} 
          className="file-input"
        />
        <button type="submit" disabled={loading || !image} className="upload-button">
          {loading ? 'Uploading...' : 'Upload and Predict'}
        </button>
      </form>

      {image && (
        <div className="image-preview">
          <h3>Uploaded Image:</h3>
          <img src={URL.createObjectURL(image)} alt="Uploaded Preview" className="uploaded-image" />
        </div>
      )}

      {error && <p className="error-text">{error}</p>}

      {response && (
        <div className="result-container">
          <h3>Prediction Result:</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
