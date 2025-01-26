import json
import spacy
import os
from google.colab import files

# Upload the domain knowledge JSON file
uploaded = files.upload()

# Get the filename from the uploaded dictionary
file_name = list(uploaded.keys())[0] 

# Specify the path to the domain knowledge JSON file (use the uploaded file name)
file_path = file_name # Update with the uploaded filename

# # Check if the file exists (This is redundant now as the file is uploaded)
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"The file '{file_path}' was not found. Please ensure it exists in the correct location.")

# Load knowledge base 
domain_knowledge = json.loads(uploaded[file_name].decode('utf-8')) # Load directly from uploaded content

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Entity extraction function
def extract_entities(text):
    doc = nlp(text)
    entities = {
        "competitors": [ent.text for ent in doc if ent.text in domain_knowledge['competitors']],
        "features": [ent.text for ent in doc if ent.text in domain_knowledge['features']],
        "pricing_keywords": [ent.text for ent in doc if ent.text in domain_knowledge['pricing_keywords']]
    }
    return entities

# Example usage
text = "CompetitorX offers an analytics solution with a great pricing model."
print(extract_entities(text))