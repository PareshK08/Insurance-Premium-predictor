
import pickle
import pandas as pd

with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#MLFlow
MODEL_VERSION = '1.0.0'

# Get class labels from model (important fro matching Probablities to class name) 
class_lables = model.classes_.tolist()

def predict_output(user_input:dict):
    
    df =pd.DataFrame([user_input])
        
    predicted_class=model.predict(df)[0]
    
    # Get probabliyties for all classes 
    probablities = model.predict_proba(df)[0]
    confidence = max(probablities)
    
    # Create Mapping {class_name:Probabliry}
    class_probs = dict(zip(class_lables,map(lambda x:round(x,4),probablities)))
    
    return{
        "Predicted_Category":predicted_class,
        "Confidence":round(confidence,4),
        "Class_Probablities":class_probs 
    }
    
    
