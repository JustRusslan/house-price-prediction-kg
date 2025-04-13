import pickle
from flask import Flask, render_template, request
import numpy as np

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission and prediction
@app.route('/', methods=["POST"])
def predict_func():
    try:
        number_of_rooms = request.form.get("Number_of_rooms", type=float)
        area_in_m2 = request.form.get("Area_in_m2", type=float)
        floor = request.form.get("Floor", type=float)

        # Format input for prediction
        X = np.array([number_of_rooms, area_in_m2, floor]).reshape(1, -1)

        # Predict and round to nearest dollar
        prediction = int(model.predict(X)[0])
        message = f"Estimated apartment price: ${prediction:,}"

    except Exception as e:
        message = f"Error: {e}"

    return render_template('index.html', prediction=message)