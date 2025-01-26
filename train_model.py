import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load preprocessed data
df = pd.read_csv('processed_dataset.csv')

# Ensure the 'labels' column is treated as strings
df['labels'] = df['labels'].astype(str)

# Convert labels to multi-label binary encoding
y = df['labels'].str.get_dummies(sep=',')

# Ensure 'clean_text' column exists and convert to string (fillna is already done during preprocessing)
df['clean_text'] = df['clean_text'].astype(str) 

# Extract the clean text
X = df['clean_text']

# Vectorize text data
vectorizer = TfidfVectorizer(max_features=5000)
X_vect = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Train the model
model = OneVsRestClassifier(LogisticRegression(max_iter=500)) 
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, 'classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Evaluate
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
print("Model trained and saved successfully.")