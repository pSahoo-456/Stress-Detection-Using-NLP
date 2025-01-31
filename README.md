# 🧠 Stress Detection using NLP & Machine Learning  

## 📌 Overview  
This project aims to detect stress levels in text-based data using Natural Language Processing (NLP) techniques and Machine Learning models. The dataset undergoes text preprocessing, feature extraction, and classification using an ensemble of machine learning classifiers.  

## 🚀 Features  
- **Text Preprocessing**: Tokenization, stopword removal, stemming, and cleaning.  
- **Word Cloud Visualization**: A graphical representation of the most common words.  
- **TF-IDF Feature Extraction**: Converts text into meaningful numerical representations.  
- **Machine Learning Models**: Uses **Naïve Bayes, Logistic Regression, Random Forest, and SVM** in an ensemble Voting Classifier.  
- **Interactive Prediction**: Users can input text to predict stress levels.  

## 📂 Dataset  
- The dataset (`stress.csv`) contains text samples labeled as **Stress (1)** or **No Stress (0)**.  
- The model maps these labels to `"Stress"` and `"No Stress"` for better interpretability.  

## 🔧 Installation & Setup  
### 1️⃣ Clone the repository  
```bash
git clone https://github.com/pSahoo-456/stress-detection.git
cd stress-detection
