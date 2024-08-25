# Bengaluru House Price Prediction

## Project Overview

This project involves predicting house prices in Bengaluru using machine learning techniques. The project consists of two main parts:

1. **Data Preprocessing and Model Training**: Analyzing and preparing data, training a machine learning model, and saving the trained model.
2. **Web Application**: A Flask web application that allows users to input house features and get predicted prices using the trained model.

## Project Structure

- **`model/`**: Contains the Jupyter Notebook (`.ipynb`) file and dataset (`Bengaluru_House_Data.csv`).
- **`server/`**: Contains the Flask application files:
  - `app.py`: The main Flask application script.
  - **`artifacts/`**: Contains the model and columns data files:
    - `banglore_home_prices_model.pickle`: The trained model.
    - `columns.json`: JSON file with feature columns.
  - **`templates/`**: Contains HTML templates:
    - `index.html`: The main HTML file for the web interface.
  - **`static/`**: Contains static files (CSS and JS).

## Setup Instructions

### 1. Using Jupyter Notebook

If you are using Jupyter Notebook, follow these steps:

#### Install Required Libraries

Open a terminal or command prompt and install the required libraries:

```bash
pip install numpy pandas tensorflow scikit-learn matplotlib
```

#### Run the Jupyter Notebook

Navigate to the `model` directory and launch Jupyter Notebook:

```bash
cd model
jupyter notebook
```

Open the `.ipynb` file in Jupyter Notebook and run the cells to preprocess data, train the model, and save it.

### 2. Using Google Colab

If you prefer Google Colab, you can run the notebook on Google Colab by following these steps:

#### Open the Notebook on Google Colab

1. Go to [Google Colab](https://colab.research.google.com/).
2. Click on **File** > **Upload notebook** and upload the `.ipynb` file from your local machine.

#### Install Required Libraries

Add a new cell at the beginning of the notebook and install the required libraries using the following commands:

```python
!pip install numpy pandas tensorflow scikit-learn matplotlib
```

#### Upload Dataset

Upload `Bengaluru_House_Data.csv` using the Colab file uploader:

```python
from google.colab import files
uploaded = files.upload()
```

Ensure you adjust the file paths in your code to match the Colab environment.

## Running the Flask Web Application

### Install Flask

Install Flask and any other dependencies needed for the server:

```bash
pip install flask
```

### Run the Flask Application

Navigate to the `server` directory and start the Flask application:

```bash
cd server
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/` on your local machine.

## How to Use

1. **Train the Model**

   Use the Jupyter Notebook or Google Colab to train the model and save it to the `server/artifacts/` directory.

2. **Web Interface**

   Open the web application in your browser. Use the interface to input house details and get the estimated price.

## Notes

- Ensure that the `artifacts` directory contains the `banglore_home_prices_model.pickle` and `columns.json` files.
- The `static` and `templates` directories should contain your CSS, JS, and HTML files as needed for the web application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
