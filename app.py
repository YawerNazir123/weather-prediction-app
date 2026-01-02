from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained pipeline
model = joblib.load("weather_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    try:
        land_avg = float(request.form["avg_temp"])
        land_max = float(request.form["max_temp"])
        land_min = float(request.form["min_temp"])

        # Validation
        if not (-30 <= land_avg <= 40):
            raise ValueError("Land Average Temperature must be between -30°C and 40°C")
        if not (-20 <= land_max <= 55):
            raise ValueError("Land Max Temperature must be between -20°C and 55°C")
        if not (-50 <= land_min <= 30):
            raise ValueError("Land Min Temperature must be between -50°C and 30°C")

        features = [[land_avg, land_max, land_min]]
        prediction = model.predict(features)

        return render_template(
            "index.html",
            result=f"{round(prediction[0], 2)} °C",
            success=True
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e),
            success=False
        )

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

