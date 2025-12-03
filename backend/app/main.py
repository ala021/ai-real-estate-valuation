from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <--- NEW IMPORT
from pydantic import BaseModel
from ml_engine.prediction import predict_house_price

app = FastAPI(title="Real Estate AI Valuation Engine")

# <--- NEW: ALLOW REACT TO CONNECT --->
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HouseRequest(BaseModel):
    size_sqm: float
    bedrooms: int
    location: str

@app.get("/")
def home():
    return {"message": "AI Real Estate Engine is Running"}

@app.post("/predict")
def predict(request: HouseRequest):
    try:
        price = predict_house_price(request.size_sqm, request.bedrooms, request.location)
        return {"predicted_price": price}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))