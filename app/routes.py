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
        # Get data from form
        nitrogen = float(request.form.get('nitrogen'))
        potassium = float(request.form.get('potassium'))
        ph = float(request.form.get('ph'))
        rainfall = float(request.form.get('rainfall'))
        temperature = float(request.form.get('temperature'))

        # Create a DataFrame for the model
        input_data = pd.DataFrame([[nitrogen, potassium, ph, rainfall, temperature]], 
                                  columns=['Nitrogen', 'Potassium', 'pH', 'Rainfall', 'Temperature'])

        # Predict using the model
        prediction = model.predict(input_data)

        return render_template('result.html', prediction=prediction[0])

    return render_template('index.html')
