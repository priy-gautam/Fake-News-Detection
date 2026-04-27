Truth Lens – Fake News Detection System
Overview

Truth Lens is a machine learning web application built using Streamlit that detects whether a news article is fake or real. The system uses natural language processing techniques and a trained machine learning model to analyze text and provide predictions with confidence scores.

The main goal of this project is to help users identify misinformation and verify the authenticity of news content.

Features
Machine learning-based fake news detection
Confidence score for each prediction
Real-time text analysis
Prediction history tracking
Simple and interactive Streamlit interface
Multi-page navigation (Home, About, Prediction)
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
└── README.md              Project documentation
How It Works
User enters a news article in the input field
The text is processed using TF-IDF Vectorization
The trained machine learning model analyzes the input
The system predicts whether the news is fake or real
A confidence score is displayed with the result
The prediction is stored in session history
Installation and Setup
Step 1: Clone the repository
git clone <your-repo-link>
cd fake-news-detection
Step 2: Install dependencies
pip install streamlit joblib scikit-learn
Step 3: Run the application
streamlit run app.py
Model Details
Algorithm: Logistic Regression
Feature Extraction: TF-IDF Vectorizer
Dataset: Labeled fake and real news articles
Output: Binary classification (Fake or Real)
Application Pages
Home Page

Provides an introduction to the project and its purpose.

About Page

Explains the machine learning model, dataset, and technologies used.

Prediction Page

Allows users to input news text, view prediction results, confidence score, and history of previous predictions.
