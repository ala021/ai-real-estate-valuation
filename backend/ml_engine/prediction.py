import torch
import joblib
import numpy as np
import os
import torch.nn as nn

# 1. Define the same architecture as training (Required to load weights)
class PricePredictionModel(nn.Module):
    def __init__(self, input_dim):
        super(PricePredictionModel, self).__init__()
        self.layer_1 = nn.Linear(input_dim, 64)
        self.layer_2 = nn.Linear(64, 32)
        self.layer_3 = nn.Linear(32, 1)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        return self.layer_3(x)

# 2. Global variables to hold the loaded model
model = None
scaler_X = None
scaler_y = None
le = None

def load_artifacts():
    """Loads the model and scalers from disk into memory."""
    global model, scaler_X, scaler_y, le
    
    # Paths
    base_path = "ml_engine/models"
    
    # Load Scalers
    scaler_X = joblib.load(f"{base_path}/scaler_X.pkl")
    scaler_y = joblib.load(f"{base_path}/scaler_y.pkl")
    le = joblib.load(f"{base_path}/label_encoder.pkl")
    
    # Load Model
    # We need to know the input dimension (size_sqm, bedrooms, location) = 3 inputs
    model = PricePredictionModel(input_dim=3)
    model.load_state_dict(torch.load(f"{base_path}/price_model.pth"))
    model.eval() # Set to evaluation mode
    print("✅ AI Model loaded into memory.")

def predict_house_price(size_sqm, bedrooms, location):
    """
    Takes raw inputs, scales them, runs the AI, and returns the real price.
    """
    if model is None:
        load_artifacts()
        
    # 1. Prepare Input
    try:
        loc_encoded = le.transform([location])[0]
    except ValueError:
        # If location is unknown, default to 'City Center' (or handle error)
        loc_encoded = le.transform(['City Center'])[0]
        
    raw_input = np.array([[size_sqm, bedrooms, loc_encoded]])
    
    # 2. Scale Input (The AI expects small numbers)
    input_scaled = scaler_X.transform(raw_input)
    input_tensor = torch.tensor(input_scaled, dtype=torch.float32)
    
    # 3. Predict
    with torch.no_grad():
        prediction_scaled = model(input_tensor)
    
    # 4. Unscale Output (Convert back to Dollars/Lira)
    predicted_price = scaler_y.inverse_transform(prediction_scaled.numpy())
    
    return round(float(predicted_price[0][0]), 2)