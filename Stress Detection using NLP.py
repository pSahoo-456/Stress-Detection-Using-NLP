

import pandas as pd
import numpy as np
import nltk
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Load the dataset
data = pd.read_csv("/content/stress.csv")
print(data.head())

# Check for null values
print(data.isnull().sum())

# Download NLTK stopwords
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords
import string

# Set of stopwords
stopword = set(stopwords.words('english'))

# Define the clean function
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text

# Clean the text data
data["text"] = data["text"].apply(clean)

# Generate a word cloud
text = " ".join(i for i in data.text)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Map labels to "No Stress" and "Stress"
data["label"] = data["label"].map({0: "No Stress", 1: "Stress"})
data = data[["text", "label"]]
print(data.head())

# Feature extraction and train-test split
x = np.array(data["text"])
y = np.array(data["label"])

# Feature extraction with TF-IDF and n-grams
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
X = tfidf.fit_transform(data["text"])
y = data["label"]

# Train-test split
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.ensemble import VotingClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Ensemble model: Voting Classifier
bnb = BernoulliNB()
lr = LogisticRegression(max_iter=200)
rf = RandomForestClassifier(n_estimators=200)
svm = SVC(probability=True)

voting_clf = VotingClassifier(estimators=[
    ('bnb', bnb),
    ('lr', lr),
    ('rf', rf),
    ('svm', svm)
], voting='soft')

# Train and evaluate the ensemble model
voting_clf.fit(xtrain, ytrain)
accuracy = voting_clf.score(xtest, ytest)
print(f"Ensemble Model Accuracy: {accuracy * 100:.2f}%")

# Function to predict stress or no stress
def predict_stress(sentence):
    cleaned_sentence = clean(sentence)
    transformed_sentence = tfidf.transform([cleaned_sentence])
    prediction = voting_clf.predict(transformed_sentence)
    return prediction[0]

# Example usage
user_input = "I have so much work to do and I don't know where to start!"
prediction = predict_stress(user_input)
print(f"The input sentence is predicted to be: {prediction}")

# Example usage with random user input
user_input = input("Enter a Text: ")
prediction = predict_stress(user_input)
print(f"The input sentence is predicted to be: {prediction}")

