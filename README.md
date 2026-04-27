Truth Lens – Fake News Detection System
Overview

Truth Lens is a machine learning-based web application built using Streamlit that detects whether a news article is fake or real. It uses natural language processing techniques and a trained machine learning model to analyze text and provide predictions with confidence scores.

The purpose of this project is to help users identify misinformation and improve awareness in digital media.

Features
AI-based fake news detection
Confidence score for predictions
Real-time text analysis
Prediction history tracking
Simple Streamlit interface
Tab-based navigation (Home, About, Prediction)
Technologies Used
Python
Streamlit
Scikit-learn
Natural Language Processing (TF-IDF Vectorization)
Joblib
Logistic Regression
Project Structure
fake-news-detection/
│
├── app.py                  Main Streamlit application
├── fake_news_model.pkl    Trained machine learning model
├── requirements.txt       Project dependencies
└── README.md              Documentation file
How It Works
User enters a news article in the input box
Text is converted into numerical features using TF-IDF
Machine learning model predicts whether the news is fake or real
Confidence score is generated
Result is displayed and stored in session history
How to Run the Project
Step 1: Install dependencies
pip install streamlit joblib scikit-learn
Step 2: Run the application
streamlit run app.py
Model Details
Algorithm: Logistic Regression
Feature Extraction: TF-IDF Vectorizer
Training Data: Labeled dataset of fake and real news
Output: Binary classification (Fake or Real)
Application Modules
Home Page
Introduction to the project
Overview of features
About Page
Explanation of machine learning model
Technology stack used
System description
Prediction Page
Input news text
Prediction result
Confidence score
History of predictions
