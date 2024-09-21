from flask import Flask, render_template, jsonify, request
import json
import pickle
import numpy as np

app = Flask(__name__)

# Global variables
__locations = None
__data_columns = None
__model = None

# Load artifacts function
def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    try:
        # Load column data
        with open("./artifacts/columns.json", "r") as f:
            data = json.load(f)
            __data_columns = data['data_columns']
            __locations = __data_columns[3:]  # Assuming locations are after the first 3 columns
        
        # Load model
        with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
            __model = pickle.load(f)
    except Exception as e:
        print(f"Error loading artifacts: {e}")

# Function to get estimated price
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

# Flask route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route to get location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({'locations': __locations})

# Flask route to predict home price
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data received")

        location = data['location']
        sqft = data['total_sqft']
        bhk = data['bhk']
        bath = data['bath']

        if not location or not isinstance(sqft, (int, float)) or not isinstance(bhk, int) or not isinstance(bath, int):
            raise ValueError("Invalid input data")

        predicted_price = get_estimated_price(location, sqft, bhk, bath)
        return jsonify({'estimated_price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Load artifacts before every request
@app.before_request
def before_request():
    if __data_columns is None or __locations is None or __model is None:
        load_saved_artifacts()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
