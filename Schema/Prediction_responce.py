from typing import Dict
from pydantic import BaseModel ,Field

class PredictionResponce(BaseModel):
    Predicted_Category :str = Field(
        ...,
        description="The predicted insurance premium catagory",
        examples="High"
    )
    
    Confidence:float= Field(
        ...,
        description="Models Confidence Score (0-1)",
        examples=8.1010
    )
    
    Class_Probablities:Dict[str,float]=Field(
        ...,
        description="Probablity description across all possible classes",
        examples={"Low":0.01,"Medium":0.15,"High":0.84}
        
    )