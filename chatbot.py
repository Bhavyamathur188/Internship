import nltk
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Download required nltk data
nltk.download('punkt')

# Step 1: Prepare training data
training_data = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you later", "goodbye", "take care"],
    "thanks": ["thanks", "thank you", "much appreciated"],
    "about_python": ["what is python", "who created python", "history of python", "tell me about python"],
    "about_nlp": ["what is nlp", "define natural language processing", "what does nlp mean"],
}

responses = {
    "greeting": ["Hello there!", "Hi! How can I help you?"],
    "goodbye": ["Goodbye!", "See you next time!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "about_python": ["Python is a programming language created by Guido van Rossum."],
    "about_nlp": ["NLP stands for Natural Language Processing. It helps computers understand human language."]
}

# Step 2: Prepare data for training
X = []
y = []

for intent, phrases in training_data.items():
    for phrase in phrases:
        X.append(phrase)
        y.append(intent)

# Step 3: Text vectorization and model training
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

# Step 4: Chatbot function
def chatbot_response(user_input):
    user_input = user_input.lower()
    input_vector = vectorizer.transform([user_input])
    predicted_intent = model.predict(input_vector)[0]
    return random.choice(responses[predicted_intent])

# Step 5: Chat loop
print("🤖 Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "exit":
        print("🤖 Bot: Goodbye!")
        break
    print("🤖 Bot:", chatbot_response(user_input))
