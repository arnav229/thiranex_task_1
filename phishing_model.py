from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Dummy dataset (Replace with an actual CSV load via pandas if available)
emails = [
    "Verify your account immediately to avoid suspension.",
    "Hey, are we still meeting for lunch today at 1 PM?",
    "Dear customer, click here to claim your $1000 gift card now!",
    "The quarterly financial reports have been uploaded to the shared drive.",
    "Urgent security alert: Update your banking password via this link.",
    "Please review the attached project proposal before tomorrow's meeting."
]
labels = [1, 0, 1, 0, 1, 0]  # 1 = Phishing, 0 = Safe

# Split data
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.33, random_state=42)

# Vectorize text features
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predictions
predictions = model.predict(X_test_tfidf)

# Evaluation
print("Accuracy Score:", accuracy_score(y_test, predictions))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

# Test Sample
test_email = ["Click this link to reset your bank password immediately"]
test_vector = vectorizer.transform(test_email)
pred = model.predict(test_vector)
print(f"\nTest Prediction for '{test_email[0]}': {'Phishing' if pred[0] == 1 else 'Safe'}")
