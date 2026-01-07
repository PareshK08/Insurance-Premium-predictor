#Insurance Premium Prediction Service
A local full-stack Machine Learning application that predicts insurance premium categories (Low, Medium, or High) based on user health and demographic data. This project demonstrates the integration of a Scikit-Learn pipeline with a FastAPI backend and a Streamlit user interface.

🚀 Project Overview
This project bridges the gap between a static ML model and a functional application. It features a decoupled architecture where the frontend (Streamlit) communicates with a local REST API (FastAPI) to serve real-time predictions.

Key Features
Predictive Modeling: Achieved 90% accuracy using a Random Forest Classifier.

Automated Feature Engineering: Real-time calculation of BMI, Age Groups, and Lifestyle Risk tiers within the API layer.

Data Validation: Implemented strict type-checking and validation using Pydantic schemas.

Decoupled Architecture: Separated the inference engine from the UI for a modular, professional codebase.

🛠️ Technical Stack
Machine Learning: Python, Scikit-Learn, Pandas, NumPy

API/Backend: FastAPI, Pydantic, Uvicorn

Frontend UI: Streamlit

Model Serialization: Pickle

📂 Project Structure
Plaintext

├── model/
│   ├── insurance_model.pkl    # Trained Scikit-Learn Pipeline
│   └── model_building.ipynb   # Model training & Feature Engineering logic
├── app.py                     # FastAPI backend (Inference Engine)
├── frontend.py                # Streamlit UI
└── requirements.txt           # Project dependencies
⚙️ How to Run Locally
1. Clone the Repository
Bash

git clone https://github.com/your-username/insurance-premium-prediction.git
cd insurance-premium-prediction
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Start the FastAPI Server
In your first terminal, run:

Bash

uvicorn app:app --reload
The API will be live at http://127.0.0.1:8000

4. Start the Streamlit UI
In a second terminal, run:

Bash

streamlit run frontend.py
The UI will open in your browser at http://localhost:8501

📈 Learning Outcomes
Inference Pipelines: Learned to handle model inference in a production-style environment.

Schema Enforcement: Mastered using Pydantic to ensure the model never receives "dirty" or invalid data.

Decoupling: Understood the importance of separating the UI from the business logic for scalability.
