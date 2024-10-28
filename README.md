# Soil Type Detection for Gujarat Soils

Welcome to the Soil Type Detection project! This application identifies soil types specific to the Gujarat region by analyzing images and predicting soil type along with a confidence score. The project consists of a frontend built with React.js and a Flask API backend that processes the image to make predictions.

## Features

- **Soil Type Prediction**: Upload an image to receive a prediction of soil type and a confidence score.
- **User-Friendly Interface**: Simple and intuitive interface for uploading soil images and viewing predictions.
- **Region-Specific Classifications**: Classifies soil types unique to Gujarat, such as *Goradu Jamin*, *Kaadi Jamin*, *Kanp ni jamin*, and others.
- **REST API**: Flask API processes the image and returns a JSON response with prediction results.

## Technologies Used

- **Frontend**: React.js
- **Backend**: Flask
- **Machine Learning**: CNN model with TensorFlow and Keras
- **IDEs**: Visual Studio Code, PyCharm
- **Testing**: Postman for API testing
- **Virtual Environment**: Python Virtual Environment for managing dependencies (Windows)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pe4rl10/Soil_Type_Detection_for_Gujarat_Soils.git
   ```

2. **Backend Setup**:

- Navigate to the backend directory
    ```bash
    cd backend
    ```
- Create a virtual environment (Windows):
    ```bash
    python -m venv venv
    ```
- Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```
- Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. **Frontend Setup**:
- Navigate to the frontend directory:
    ```bash
    cd ..
    cd frontend
    ```
- Install Node modules:
    ```bash
    npm install
    ```
4. **Run the Application**:
- **Backend**: Start the Flask server:
    ```bash
    flask run
    ```
- **Frontend**: Start the React application::
    ```bash
    npm run dev
    ```
5. **Access the Application**: Open your web browser and navigate to `http://localhost:5173` to use the application.

## Usage
- Upload an image of soil to receive a prediction of the soil type and a confidence score.
- View the prediction and confidence score displayed on the frontend interface.

## Contributing

Contributions to Soil Type Detection project are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.

