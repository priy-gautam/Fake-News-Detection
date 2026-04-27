import streamlit as st
import joblib
from datetime import datetime

# Load the model
model = joblib.load("fake_news_model.pkl")

# Initialize history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to classify news
def classify_news(text):
    prediction = model.predict([text])[0]
    confidence = model.predict_proba([text]).max() * 100
    return prediction, confidence

# Page config
st.set_page_config(page_title="Truth Lens", layout="wide")

# Dropdown tab selector
selected_tab = st.selectbox("Navigate to:", ["Home", "About", "Prediction"])

# ---------- HOME ----------
if selected_tab == "Home":
    st.markdown("<h1 style='text-align: center; color: #4A4A4A;'>📰 Truth Lens</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #6A5ACD;'>Smart Fake News Detection using Machine Learning</h3>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([2, 3])

    with col1:
        st.image(
            "https://t3.ftcdn.net/jpg/02/11/18/42/360_F_211184264_WUTdv0iIBQqYHHRasi70MwU7m0WEw20J.jpg",
            caption="Image Source: Adobe Stock",
            use_container_width=True
        )

    with col2:
        st.markdown("""
        <div style='font-size: 18px; line-height: 1.8;'>
            <p><b>Truth Lens</b> is a smart fake news detection system powered by advanced <b>machine learning</b> and <b>natural language processing</b>.</p>
            <p>In today's digital era, misinformation spreads faster than ever. Truth Lens helps you detect fake news and verify authenticity instantly.</p>
            <p>Whether you're a student, journalist, or a responsible digital citizen, our tool helps you stay informed and accurate in your online decisions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔍 What Truth Lens Offers:")
    st.markdown("""
    - 🧠 AI-powered news authenticity classification  
    - ✅ Prediction confidence score  
    - 📊 History with summary stats (Fake vs Real)  
    - 🧾 Simple, elegant, tab-based interface  
    """)

    st.success("Be informed. Be responsible. Verify before sharing.")
    st.markdown("---")
    st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit and Scikit-learn</p>", unsafe_allow_html=True)

# ---------- ABOUT ----------
elif selected_tab == "About":
    st.markdown("<h2 style='color: #6A5ACD;'>About Truth Lens</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size: 17px; line-height: 1.7;'>
        <p><b>Truth Lens</b> is a machine learning web application that helps users detect fake news articles in real time.</p>
        <p>This project was created to combat the growing spread of misinformation in digital media.</p>
        <p><b>How it Works:</b></p>
        <ul>
            <li>Trained on thousands of real and fake news articles</li>
            <li>Uses <b>TF-IDF Vectorization</b> to convert text to numerical data</li>
            <li>Utilizes a <b>Logistic Regression</b> classifier for accurate prediction</li>
        </ul>
        <p>It’s ideal for students, researchers, journalists, or anyone who wants to verify news quickly and accurately.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👨‍💻 Developed Using:")
    st.markdown("""
    - 🐍 Python  
    - 📚 Scikit-learn  
    - 📊 Streamlit  
    - 📄 TF-IDF (Text Features)  
    - 💾 joblib (for model saving/loading)  
    """)

# ---------- PREDICTION ----------
elif selected_tab == "Prediction":
    st.markdown("<h2 style='color: #6A5ACD;'>📝 Enter News Article Below</h2>", unsafe_allow_html=True)

    news_input = st.text_area("Paste your news text here", height=200)

    if st.button("Analyze"):
        if news_input.strip() == "":
            st.warning("Please enter some text to analyze.")
        else:
            result, confidence = classify_news(news_input)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            st.session_state.history.append({
                "text": news_input,
                "result": result,
                "confidence": round(confidence, 2),
                "time": timestamp
            })

            if result == "FAKE":
                st.error(f"🛑 FAKE NEWS ({confidence:.2f}% confidence)")
                if confidence > 90:
                    st.warning("⚠️ High Confidence: This news appears to be strongly fake!")
            else:
                st.success(f"✅ REAL NEWS ({confidence:.2f}% confidence)")

            st.markdown("---")

    # Show prediction history
    if st.session_state.history:
        st.markdown("### 📚 Prediction History")
        fake_count = sum(1 for h in st.session_state.history if h['result'] == 'FAKE')
        real_count = sum(1 for h in st.session_state.history if h['result'] == 'REAL')
        st.info(f"Total Predictions: {len(st.session_state.history)} | 🛑 Fake: {fake_count} | ✅ Real: {real_count}")

        for h in reversed(st.session_state.history[-5:]):
            badge_color = "#FF6347" if h["result"] == "FAKE" else "#90EE90"
            st.markdown(f"""
                <div style="border-left: 5px solid {badge_color}; padding: 10px; margin-bottom: 10px; background-color: #f9f9f9;">
                    <b>{h["time"]}</b><br>
                    <b>Prediction:</b> {h["result"]} ({h["confidence"]}%)<br>
                    <b>Text:</b> {h["text"][:100]}...
                </div>
            """, unsafe_allow_html=True)
