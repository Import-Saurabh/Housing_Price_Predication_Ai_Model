🏠 Housing Price Prediction Model

A machine learning-powered web application that predicts house prices in Bengaluru based on key property features.
This project brings together data science and web development to deliver accurate real estate price estimations with an intuitive interface.

✨ Features

Accurate Predictions: Ridge Lasso Regression models and XG Boost trained on cleaned Bengaluru housing data, achieving an R² test score of 0.87

User-Friendly Interface: Simple and responsive web form for inputting property details.

Location-Based Estimates: Supports multiple neighborhoods across Bengaluru.

Real-Time Results: Instant price predictions without page refresh.

🛠️ Tech Stack

Backend

Python 3.12.1 – Core programming language

Flask – Web framework

Pandas & NumPy – Data manipulation and analysis

Scikit-learn – Machine learning library

Pickle – Model serialization , XG Boost

Frontend

HTML5 – Page structure

Bootstrap 4 – Responsive styling

JavaScript – Form handling & AJAX requests

Machine Learning

Data Cleaning – Comprehensive preprocessing pipeline

Feature Engineering – Price per sqft, BHK normalization

Model Training – Ridge, Lasso Regression and XG Boost(R² = 0.87)

Outlier Handling – Advanced statistical methods for improved data quality

📊 Dataset

The model is trained on the Bengaluru House Data dataset:

13,320 initial entries

7,361 cleaned entries after preprocessing

Key Features: Location, total square footage, BHK, bathrooms, price

Data Processing Steps

Missing Value Handling: Strategic imputation for location, size, and bathroom data

Feature Engineering: Derived features like BHK count and price per sqft

Outlier Removal:

Statistical detection (mean ± standard deviation)

BHK-based price consistency checks

Minimum square footage validation (300 sqft per BHK)

Location Consolidation: Grouped rare/low-frequency locations into an “other” categor
