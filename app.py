from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load("models/random_forest_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        input_data = np.array([features])
        prediction = model.predict(input_data)
        result = "Fraudulent" if prediction[0] == 1 else "Legit"
        return render_template("index.html", prediction_text=f"Transaction is {result}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
