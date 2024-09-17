from flask import Blueprint, render_template, request
import pickle
import pandas as pd

main = Blueprint('main', __name__)

# Load the machine learning model
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from form with default value handling
        nitrogen = request.form.get('nitrogen')
        potassium = request.form.get('potassium')
        pH = request.form.get('pH')
        rainfall = request.form.get('rainfall')
        temperature = request.form.get('temperature')

        # Check if any of the required fields are missing or empty
        if not all([nitrogen, potassium, pH, rainfall, temperature]):
            return "Please fill in all the fields."

        try:
            # Convert data to float
            nitrogen = float(nitrogen)
            potassium = float(potassium)
            pH = float(pH)
            rainfall = float(rainfall)
            temperature = float(temperature)
        except ValueError:
            return "Please enter valid numerical values."

        # Create a DataFrame for the model
        input_data = pd.DataFrame([[nitrogen, potassium, pH, rainfall, temperature]], 
                                  columns=['N', 'K', 'pH', 'rainfall', 'temperature'])

        # Predict using the model
        prediction = model.predict(input_data)

        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')
