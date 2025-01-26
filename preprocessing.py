# @title Default title text
import pandas as pd
import spacy
import re
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Load dataset, specifying header and names
path = "/content/drive/MyDrive/Dataset/DataSet.csv"
df = pd.read_csv(path, encoding='utf-8', delimiter=',', header=None, names=['id', 'text_snippet', 'labels']) 
# header=None tells Pandas there's no header row in the file
# names=['id', 'text_snippet', 'labels'] provides the column names

# Verify column names
print("Columns in dataset:", df.columns)

# Preprocess text function
def preprocess_text(text):
    # Handle potential missing or non-string values
    if isinstance(text, float) and pd.isna(text):
        return "" # Or any placeholder you prefer
    elif not isinstance(text, str):
        return str(text) # Convert to string if not already
    
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    doc = nlp(text)
    # Modified condition to keep tokens that are not stopwords OR have alphanumeric characters
    tokens = [token.lemma_ for token in doc if token.text.lower() not in stopwords.words('english') or token.text.isalnum()]
    return " ".join(tokens)

# Apply preprocessing
df['clean_text'] = df['text_snippet'].apply(preprocess_text)  
df.to_csv('processed_dataset.csv', index=False)
print("Preprocessing completed and saved to processed_dataset.csv.")