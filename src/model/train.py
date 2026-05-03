from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib   
import pickle
import os


# Ensure artifacts folder exists
os.makedirs("artifacts", exist_ok=True)

# Load dataset
X, y = load_iris(return_X_y=True)

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("artifacts/model.pkl", "wb") as f:   # wb stands for "write binary
    pickle.dump(model, f)

print("✅ Model saved at artifacts/model.pkl")