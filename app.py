from flask import Flask, request, render_template
import numpy as np
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")  # Show form

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get all 30 input features from the form
        features = [float(request.form[f"feature{i+1}"]) for i in range(30)]
        features_array = np.array(features).reshape(1, -1)
        
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0][1]

        result = "Fraud" if prediction == 1 else "Not Fraud"

        return render_template("index.html", prediction_text=f"Prediction: {result} (Probability: {probability:.2f})")
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
