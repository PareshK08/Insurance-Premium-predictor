# Insurance Premium Prediction Service

A local full-stack Machine Learning application that predicts insurance premium categories (**Low**, **Medium**, or **High**) based on demographic and health data. This project showcases a modular architecture using **FastAPI** for the backend and **Streamlit** for the frontend.



## 🚀 Project Highlights
* **Model Performance:** Developed a Random Forest classifier achieving **90% accuracy** on test data.
* **Feature Engineering:** Implemented automated real-time calculations for BMI, Age Groups, and Lifestyle Risk within the API layer.
* **Data Integrity:** Utilized **Pydantic** to enforce 100% data validation, ensuring robust handling of user inputs.
* **Architecture:** Built a decoupled Backend (API) and Frontend (UI) system to simulate professional software environments.

## 🛠️ Technical Stack
* **Language:** Python
* **ML Libraries:** Scikit-Learn, Pandas, NumPy
* **API Framework:** FastAPI, Uvicorn, Pydantic
* **Web UI:** Streamlit

---

## 📂 Project Structure
```text
├── model/
│   ├── model.pkl            # Trained Scikit-Learn Pipeline
│   └── notebook.ipynb       # Feature engineering & training logic
├── app.py                   # FastAPI backend & inference logic
├── frontend.py              # Streamlit UI 
└── requirements.txt         # Project dependencies
