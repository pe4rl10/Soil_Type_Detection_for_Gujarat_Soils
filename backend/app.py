from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
from flask_cors import CORS  # Import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the pre-trained model
MODEL_PATH = 'soil_detection_model-15ep.h5'
model = load_model(MODEL_PATH)

# Define image size based on model input size
IMG_HEIGHT, IMG_WIDTH = 224, 224

# Define class labels (based on your dataset)
class_names = ['Goradu Jamin', 'Kaadi Jamin', 'Kanp ni jamin', 'Laal jamin', 'North Gujarat', 'South Gujarat (New)']


# Define a route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure an image is provided
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        # Ensure the file is an image
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Load and preprocess the image
        image = Image.open(file)
        image = image.resize((IMG_HEIGHT, IMG_WIDTH))  # Resize to model input size
        image = img_to_array(image)  # Convert to array
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        image = image / 255.0  # Normalize pixel values

        # Make prediction using the model
        prediction = model.predict(image)
        predicted_class_idx = np.argmax(prediction, axis=1)[0]
        predicted_class_name = class_names[predicted_class_idx]  # Map index to class name

        # Prepare response with class name and confidence
        response = {
            'predicted_class': predicted_class_name,
            'confidence': float(np.max(prediction))  # Highest probability as confidence score
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# ['Goradu Jamin', 'Kaadi Jamin', 'Kanp ni jamin', 'Laal jamin', 'North Gujarat', 'South Gujarat (New)']