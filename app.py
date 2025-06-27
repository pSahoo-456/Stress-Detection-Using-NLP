# app.py
import streamlit as st
import joblib
import nltk
import re
import string

# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load model and vectorizer
model = joblib.load("stress_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@w+|\#','', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)

def predict_stress(text):
    cleaned = clean_text(text)
    vect_text = vectorizer.transform([cleaned])
    prediction = model.predict(vect_text)
    return prediction[0]

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="Stress Detector", layout="centered")

st.title("😟 Stress Detection from Text 💬")
st.write("🔍 Enter a sentence to find out if it's **Stressful** or **Not Stressful**.")

user_input = st.text_area("Enter your text here:")

if st.button("Detect Stress"):
    if user_input.strip() != "":
        result = predict_stress(user_input)
        if result == "Stress":
            st.error("🚨 Stress Detected in the text!")
        else:
            st.success("✅ No Stress Detected in the text.")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
