import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 5000
LOCATIONS = ['Downtown', 'Suburban', 'Rural', 'City Center', 'Industrial']

def generate_housing_data():
    np.random.seed(42)
    sizes = np.random.normal(loc=120, scale=40, size=NUM_SAMPLES)
    sizes = np.clip(sizes, 30, 500)
    
    bedrooms = (sizes / 25) + np.random.normal(0, 0.5, NUM_SAMPLES)
    bedrooms = np.clip(np.round(bedrooms), 1, 8).astype(int)
    
    location_data = np.random.choice(LOCATIONS, size=NUM_SAMPLES)
    
    base_prices = {'Downtown': 3500, 'City Center': 3000, 'Suburban': 2000, 'Industrial': 1500, 'Rural': 1000}
    
    prices = []
    for i in range(NUM_SAMPLES):
        loc = location_data[i]
        price = (sizes[i] * base_prices[loc]) + (bedrooms[i] * 10000) + np.random.randint(-10000, 10000)
        prices.append(round(price, 2))

    df = pd.DataFrame({
        'size_sqm': np.round(sizes, 2),
        'bedrooms': bedrooms,
        'location': location_data,
        'price': prices
    })
    
    # Saves to the main folder so the training script can find it
    df.to_csv("housing_data.csv", index=False)
    print("✅ housing_data.csv created successfully!")

if __name__ == "__main__":
    generate_housing_data()