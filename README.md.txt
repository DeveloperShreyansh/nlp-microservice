# NLP Microservice for Multi-Label Classification and Entity Extraction

## **Project Overview**
This project implements an end-to-end NLP pipeline that performs:
1. **Multi-label text classification** for sales/marketing call snippets.
2. **Entity extraction** using both dictionary lookup and Named Entity Recognition (NER).
3. **Summarization** of text snippets.
4. A REST API to expose the functionalities, containerized with Docker.

---

## **Project Structure**

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/nlp-microservice.git
cd nlp-microservice
2. Install Dependencies
Ensure you have Python 3.9+ installed, then install the required dependencies:

bash
pip install -r requirements.txt

3. Preprocess the Data
Run the text preprocessing script:

bash
python preprocessing.py
This will create processed_dataset.csv with cleaned text.

4. Train the Model
Train the multi-label classification model:

bash
python train_model.py
The trained model and vectorizer will be saved as classifier_model.pkl and vectorizer.pkl.

5. Run the REST API
Start the FastAPI server locally:

bash
uvicorn app:app --reload
The API will be available at:

Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


6. Test the API
You can test the API using curl:

bash
curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{"text_snippet":"CompetitorX offers a discount on pricing models."}'
Expected response:

json
{
  "predicted_labels": ["Pricing Discussion"],
  "extracted_entities": {
    "competitors": ["CompetitorX"],
    "features": [],
    "pricing_keywords": ["discount", "pricing models"]
  },
  "summary": "Summary: CompetitorX offers a discount on pricin..."
}


Docker Deployment Instructions
1. Build the Docker Image
Ensure Docker is installed and running, then build the image:

bash
docker build -t nlp_microservice .
2. Run the Docker Container
Once built, run the container on port 8000:

bash
docker run -p 8000:8000 nlp_microservice
3. Access the API (Inside Docker)
After running the container, you can access the API via:

http://localhost:8000/docs
http://localhost:8000/predict/ (using curl or Postman)
Example request using curl:

bash
curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d '{"text_snippet":"CompetitorY provides better AI engine."}'
