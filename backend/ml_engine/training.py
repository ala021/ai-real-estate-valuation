import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
import joblib 
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score

# Define Neural Network
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

def train_model():
    print("🚀 Starting Model Training Pipeline...")

    # Check if data exists
    if not os.path.exists("housing_data.csv"):
        print("❌ Error: housing_data.csv not found.")
        return

    df = pd.read_csv("housing_data.csv")

    # Preprocessing
    le = LabelEncoder()
    df['location_encoded'] = le.fit_transform(df['location'])

    X = df[['size_sqm', 'bedrooms', 'location_encoded']].values
    y = df['price'].values.reshape(-1, 1)

    scaler_X = StandardScaler()
    scaler_y = StandardScaler()
    
    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)

    model = PricePredictionModel(input_dim=X.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Train
    epochs = 200
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()
        
        if (epoch+1) % 50 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

    # Evaluate
    model.eval()
    with torch.no_grad():
        predictions = model(X_test_tensor)
        y_pred_real = scaler_y.inverse_transform(predictions.numpy())
        y_test_real = scaler_y.inverse_transform(y_test)
        score = r2_score(y_test_real, y_pred_real)
        print(f"✅ Training Complete. R2 Score: {score:.4f}")

    # Save Models
    os.makedirs("backend/ml_engine/models", exist_ok=True)
    torch.save(model.state_dict(), "backend/ml_engine/models/price_model.pth")
    joblib.dump(scaler_X, "backend/ml_engine/models/scaler_X.pkl")
    joblib.dump(scaler_y, "backend/ml_engine/models/scaler_y.pkl")
    joblib.dump(le, "backend/ml_engine/models/label_encoder.pkl")
    print("💾 Model saved to backend/ml_engine/models/")

if __name__ == "__main__":
    train_model()