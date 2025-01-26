from fastapi import FastAPI
import joblib
import json
# Instead of importing from a module, directly use the defined function:
# from entity_extraction import extract_entities 

# Load model and vectorizer
model = joblib.load('classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# ... (rest of the code: extract_entities function and FastAPI app) ...

# Entity extraction function (copied from your previous cell)
import spacy
# Load spaCy model (if not already loaded)
try:
    nlp
except NameError:
    nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    # Assuming 'domain_knowledge' is loaded and available
    doc = nlp(text)
    entities = {
        "competitors": [ent.text for ent in doc if ent.text in domain_knowledge['competitors']],
        "features": [ent.text for ent in doc if ent.text in domain_knowledge['features']],
        "pricing_keywords": [ent.text for ent in doc if ent.text in domain_knowledge['pricing_keywords']]
    }
    return entities

app = FastAPI()

@app.post("/predict/")
def predict(data: dict):
    text = data['text_snippet']
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    
    labels = prediction.tolist()[0]
    entities = extract_entities(text)  # Now calling the defined function

    return {
        "predicted_labels": labels,
        "extracted_entities": entities,
        "summary": f"Summary: {text[:50]}..."  # Simple summarization
    }