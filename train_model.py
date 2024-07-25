import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
# Make sure to replace 'your_dataset.csv' with the actual path to your dataset file
df = pd.read_csv('DATASET.csv')

# Assuming your dataset has columns: 'Nitrogen', 'Potassium', 'pH', 'Rainfall', 'Temperature', and 'Crop'
X = df[['N', 'K', 'pH', 'rainfall', 'temperature']]
y = df['Crop']

# Train the machine learning model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model to a file
with open('crop_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training and saving complete.")
