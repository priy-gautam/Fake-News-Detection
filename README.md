Truth Lens – Fake News Detection System
Overview

Truth Lens is a Machine Learning-based web application built using Streamlit that detects whether a news article is Fake or Real. It uses Natural Language Processing (NLP) techniques and a trained ML model to analyze text and provide predictions with confidence scores.

The goal of this project is to help users identify misinformation and promote awareness in the digital world.

Features
AI-powered Fake News Detection
Confidence score for predictions
Real-time text analysis
Prediction history tracking
Simple and user-friendly Streamlit interface
Tab-based navigation (Home, About, Prediction)
Technologies Used
Python 
Streamlit 
Scikit-learn 
NLP (TF-IDF Vectorization) 
Joblib 
Logistic Regression Model 
Project Structure
fake-news-detection/
│
├── app.py                  # Main Streamlit application
├── fake_news_model.pkl    # Trained ML model
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
How It Works
User enters a news article in the text box
Text is processed using TF-IDF Vectorizer
ML model predicts:
Fake News
Real News
Confidence score is displayed
Prediction is saved in session history
How to Run the Project
1. Install dependencies
pip install streamlit joblib scikit-learn
2. Run the app
streamlit run app.py
Model Details
Algorithm: Logistic Regression
Feature Extraction: TF-IDF Vectorizer
Trained on: Labeled dataset of real & fake news articles
Output: Binary classification (FAKE / REAL)
Application Modules
Home Page
Project introduction
Features overview
UI branding and description
About Page
Model explanation
Dataset & algorithm details
Technology stack
Prediction Page
User input text box
Fake/Real classification
Confidence score
History of predictions
