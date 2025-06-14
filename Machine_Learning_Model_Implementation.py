from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
# -----------------------------
texts = [
    "Congratulations! You've won a free lottery ticket. Click here to claim.",
    "Important: Your account has been compromised. Reset now.",
    "Hi John, can we meet tomorrow to discuss the project?",
    "Reminder: Your subscription is due next week.",
    "Urgent! You've won a new iPhone. Claim instantly.",
    "Let's have lunch tomorrow at 1 PM.",
    "Your invoice is attached. Please review it.",
    "Update your profile to receive the reward.",
    "Meeting rescheduled to 3 PM.",
    "Win cash now! No purchase required."
]
labels = ["spam", "spam", "ham", "ham", "spam", "ham", "ham", "spam", "ham", "spam"]

# -----------------------------
# Vectorize the Text Data
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = labels

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# Train Naive Bayes Model
# -----------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# Make Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluate the Model
# -----------------------------
report = classification_report(y_test, y_pred, output_dict=True)
accuracy = accuracy_score(y_test, y_pred)

# -----------------------------
# Visualize the Results 
# -----------------------------
fig, ax = plt.subplots(figsize=(6.5, 4.5))
ax.axis('off')

# Title and layout
ax.text(0, 1.0, "Spam Detection - Model Evaluation", fontsize=14, weight='bold', color='navy')
ax.text(0, 0.9, f"Accuracy: {accuracy:.2f}", fontsize=12)
ax.text(0, 0.8, f"Precision (spam): {report['spam']['precision']:.2f}", fontsize=12)
ax.text(0, 0.7, f"Recall (spam): {report['spam']['recall']:.2f}", fontsize=12)
ax.text(0, 0.6, f"F1-score (spam): {report['spam']['f1-score']:.2f}", fontsize=12)
ax.text(0, 0.5, f"Precision (ham): {report['ham']['precision']:.2f}", fontsize=12)
ax.text(0, 0.4, f"Recall (ham): {report['ham']['recall']:.2f}", fontsize=12)
ax.text(0, 0.3, f"F1-score (ham): {report['ham']['f1-score']:.2f}", fontsize=12)

# Save and show
plt.savefig("spam_model_output_clean.png", bbox_inches='tight', dpi=150)
plt.show()

# -----------------------------
# Print Predictions
# -----------------------------
print("\nSample Predictions:")
for i, text in enumerate(X_test[:3]):
    print(f"Text {i+1} ➤ Predicted: {y_pred[i]}")
