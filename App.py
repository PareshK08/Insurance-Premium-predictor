from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.User_Input import UserInput
from Schema.Prediction_responce import PredictionResponce
from Model.predict import model ,MODEL_VERSION,predict_output

app = FastAPI()

# Human Readable        
@app.get('/')
def home():
    return{"message": "Insurance Premium Predictoin"}

# Machine Readable
@app.get('/health')
def health_check():
    return{
        'status':'OK',
        'version':MODEL_VERSION,
        'model_loded': model is not None
    }


@app.post('/predict',response_model=PredictionResponce)
def predict_premium(data:UserInput):
    user_input= {
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tire,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={'responce':prediction})
    except Exception as e:
        raise JSONResponse(status_code=500,content=str(e))