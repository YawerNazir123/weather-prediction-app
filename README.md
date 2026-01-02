🌥 Weather Prediction Web Application

A machine learning–based weather prediction web app that estimates Land and Ocean Average Temperature using historical land temperature features.
The project demonstrates a complete end-to-end ML workflow: training → integration → deployment → live hosting.

🔗 Live Demo

👉 Live Application:
https://weather-prediction-app.onrender.com

👉 GitHub Repository:
https://github.com/YawerNazir123/weather-prediction-app

📌 Project Overview

This project uses a Random Forest Regression model trained on historical global temperature data to predict Land and Ocean Average Temperature based on:

Land Average Temperature

Land Maximum Temperature

Land Minimum Temperature

The trained model is deployed using Flask and hosted live on Render, with a modern weather-style user interface.

🧠 Machine Learning Details

Dataset: Global Historical Temperature Data

Target Variable:

LandAndOceanAverageTemperature

Input Features:

LandAverageTemperature

LandMaxTemperature

LandMinTemperature

Model Used:

Random Forest Regressor

Preprocessing Pipeline:

Feature Selection (SelectKBest)

Feature Scaling (StandardScaler)

Model Accuracy:

~99% on validation data

🛠 Tech Stack
Backend

Python

Flask

scikit-learn

NumPy

Joblib

Frontend

HTML

CSS (modern weather-app styling)

Smooth animations & transitions

Deployment

GitHub (version control)

Render (live hosting)

🎯 Key Features

✔ Real-time weather prediction

✔ Scientific input validation

✔ Modern cloudy weather UI

✔ Smooth animations and transitions

✔ Fully deployed and publicly accessible

✔ Clean and scalable ML pipeline

📂 Project Structure
weather-prediction-app/
│
├── app.py
├── weather_model.pkl
├── requirements.txt
├── templates/
│   └── index.html

🚀 How It Works

User enters land temperature values

Data is validated for realistic ranges

Input is passed to the trained ML pipeline

Model predicts Land & Ocean Average Temperature

Result is displayed instantly on the web interface

