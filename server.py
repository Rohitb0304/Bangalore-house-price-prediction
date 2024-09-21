from flask import Flask, render_template, jsonify, request
import json
import pickle
import numpy as np

app = Flask(__name__)

__locations = None
__data_columns = None
__model = None

@app.before_first_request
def load_saved_artifacts():
    global __data_columns
    global __locations

    # Load column data
    with open("./artifacts/columns.json", "r") as f:
        data = json.load(f)
        __data_columns = data['data_columns']
        __locations = __data_columns[3:]  # Assuming locations are after the first 3 columns

    # Load model
    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return jsonify({'locations': __locations})

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()
        location = data['location']
        sqft = data['total_sqft']
        bhk = data['bhk']
        bath = data['bath']
        predicted_price = get_estimated_price(location, sqft, bhk, bath)
        return jsonify({'estimated_price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    app.run(debug=True)