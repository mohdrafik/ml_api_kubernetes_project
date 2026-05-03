from fastapi import APIRouter 
from src.model.predict import predict

router = APIRouter()

# Define input schema
class InputData(BaseModel):
    data: list

@router.get("/")
def home():
    return {"Message": "ML API is running succesfully"}

@router.post("/predict")
def predict_api(input:InputData):
    res = predict(input.data)
    return {"prediction":res}

