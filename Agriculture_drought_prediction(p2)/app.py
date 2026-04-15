import json
import os
from flask import Flask, render_template, request, redirect
import joblib

app = Flask(__name__)

# Load ML model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "123":
        return redirect("/dashboard")

    return render_template("login.html", error="Invalid username or password")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/predict", methods=["POST"])
def predict():

    rainfall = float(request.form["rainfall"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    soil = float(request.form["soil"])
    wind = float(request.form["wind"])

    data = [[rainfall, temperature, humidity, soil, wind]]

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    # UI logic
    if prediction == 1:
        result = "⚠️ Drought Expected"
        image = "drought.gif"
        background = "drought-bg"
        solution = [
            "Use drip irrigation 💧",
            "Switch to drought-resistant crops 🌱",
            "Apply mulching 🌾",
            "Store rainwater 🌧️"
        ]
    else:
        result = "✅ No Drought"
        image = "rain.gif"
        background = "rain-bg"
        solution = [
            "Continue normal farming 🌿",
            "Maintain irrigation 💧"
        ]

    # Severity
    if probability < 30:
        severity = "Low Risk"
    elif probability < 60:
        severity = "Moderate Risk"
    else:
        severity = "Severe Drought"

    # Model info
    if os.path.exists("model_info.json"):
        with open("model_info.json", "r") as f:
            model_info = json.load(f)
        model_name = model_info.get("model", "Unknown")
        accuracy = round(model_info.get("accuracy", 0) * 100, 2)
    else:
        model_name = "Random Forest"
        accuracy = "N/A"

    # Dummy metrics for UI graph
    rf_metrics = [0.92, 0.90, 0.91, 0.90]
    lr_metrics = [0.85, 0.83, 0.84, 0.83]

    return render_template(
        "result.html",
        prediction=result,
        probability=round(probability, 2),
        severity=severity,
        image=image,
        background=background,
        solution=solution,
        model_name=model_name,
        accuracy=accuracy,
        rf_metrics=rf_metrics,
        lr_metrics=lr_metrics
    )


if __name__ == "__main__":
    app.run(debug=True)