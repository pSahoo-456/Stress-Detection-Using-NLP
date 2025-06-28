# 🧠 Stress Detection using NLP & Machine Learning

Welcome to the **Stress Detection** project! This repository uses cutting-edge Natural Language Processing (NLP) and Machine Learning techniques to detect whether a given text expresses **stress** or **no stress**. Built with real-world applications in mind, this system processes raw text, extracts features, and predicts stress levels using an ensemble of powerful classifiers.

---

## 📌 Overview

Mental health is one of the most significant challenges of the modern era. This project aims to automatically detect stress in written text — such as social media posts, emails, or journal entries — using a pipeline of text preprocessing, feature extraction, and machine learning models.

---

## 🚀 Key Features

- 🔠 **Text Preprocessing**  
  Tokenization, stopword removal, stemming, and special character cleaning using **NLTK**.

- ☁️ **Word Cloud Visualization**  
  Visualizes the most frequent words in stress-related and non-stress text using **Matplotlib** & **WordCloud**.

- 🧮 **TF-IDF Vectorization**  
  Converts cleaned text into numerical features using **TfidfVectorizer** with n-grams for context.

- 🤖 **Machine Learning Ensemble**  
  Combines **Naïve Bayes**, **Logistic Regression**, **Random Forest**, and **SVM** via a **Voting Classifier** for improved accuracy.

- 🧪 **Interactive Prediction**  
  A simple method to pass user input and predict if it indicates **Stress** or **No Stress**.

---

## 📂 Dataset

- **File Name:** `stress.csv`  
- **Columns:**  
  - `text`: Textual content from online sources  
  - `label`: Binary class (0 = No Stress, 1 = Stress)  
  - Additional features like `confidence`, `syntax_grade`, `liwc_metrics` are available in extended versions

---

## 🛠️ Tech Stack

| Category        | Tools/Libraries                                   |
|-----------------|---------------------------------------------------|
| Language        | Python 🐍                                         |
| NLP             | NLTK, Regex                                       |
| ML Algorithms   | Logistic Regression, Naïve Bayes, Random Forest, SVM |
| Visualization   | Matplotlib, WordCloud                             |
| Feature Extraction | TfidfVectorizer                               |
| Interface (Optional) | Streamlit for deployment                    |

---

## 📊 Results

- ✅ Ensemble Voting Classifier
- 📈 Accuracy: ~85% after feature engineering and tuning
- 🧪 Accepts real-time sentence input from users

---

## 🧪 Sample Prediction

```python
predict_stress("I feel overwhelmed with everything happening in my life.")
# Output: 'Stress'





📁 Project Structure
Copy
Edit
📦 Stress-Detection-NLP
 ┣ 📄 stress.csv
 ┣ 📄 model.pkl
 ┣ 📄 tfidf.pkl
 ┣ 📄 app.py  ← Streamlit web app
 ┣ 📄 model_training.ipynb
 ┗ 📄 README.md


 📜 License
This project is open-source under the MIT License.


⭐️ Show your support!
If you like this project, consider giving it a ⭐ on GitHub. Your support motivates us to improve and expand the project!


