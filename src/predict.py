import numpy as np
import pandas as pd
import joblib

# Load models
kmeans = joblib.load(r"D:\VNSGU_PDA2\Data-Analytics-using-Python-Minor-Project\models\kmeans_model.pkl")
scaler = joblib.load(r"D:\VNSGU_PDA2\Data-Analytics-using-Python-Minor-Project\models\scaler.pkl")

# Expected column order (must match training)
features = [
    "JAVA_Total",
    "NET_Total",
    "MAD_Total",
    "IOT_Total",
    "OSS_Total",
    "CC_Total",
    "BMP_Total"
]

print("Enter Student Marks:")

new_student = {
    "JAVA_Total": float(input("JAVA Total: ")),
    "NET_Total": float(input("NET Total: ")),
    "MAD_Total": float(input("MAD Total: ")),
    "IOT_Total": float(input("IOT Total: ")),
    "OSS_Total": float(input("OSS Total: ")),
    "CC_Total": float(input("CC Total: ")),
    "BMP_Total": float(input("BMP Total: "))
}

# Convert to dataframe with correct order
new_df = pd.DataFrame([new_student])[features]

# Scale input
new_scaled = scaler.transform(new_df)

# Predict cluster
cluster = kmeans.predict(new_scaled)[0]

performance_map = {
    0: "Average Performer",
    1: "High Performer",
    2: "Needs Improvement"
}

print("\nPredicted Performance Level:", performance_map.get(cluster, "Unknown"))