import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    if __data_columns is None or __model is None:
        raise ValueError("Model or data columns not loaded.")

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

def get_location_names():
    if __locations is None:
        raise ValueError("Location data not loaded.")
    return __locations

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    # Load column data
    try:
        with open("./artifacts/columns.json", "r") as f:
            data = json.load(f)
            __data_columns = data['data_columns']
            __locations = __data_columns[3:]  # Assuming locations are after the first 3 columns
    except Exception as e:
        raise RuntimeError(f"Error loading columns: {e}")

    # Load model
    try:
        with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
            __model = pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Error loading model: {e}")

if __name__ == "__main__":
    load_saved_artifacts()
    print("Locations:", get_location_names())
    print("Estimated Price (1st Phase JP Nagar, 1000 sqft, 3 BHK, 3 Bath):", get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print("Estimated Price (1st Phase JP Nagar, 1000 sqft, 2 BHK, 2 Bath):", get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print("Estimated Price (Kalhalli, 1000 sqft, 2 BHK, 2 Bath):", get_estimated_price('Kalhalli', 1000, 2, 2))
    print("Estimated Price (Ejipura, 1000 sqft, 2 BHK, 2 Bath):", get_estimated_price('Ejipura', 1000, 2, 2))