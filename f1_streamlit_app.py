import streamlit as st
import pandas as pd
import numpy as np
import fastf1
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
import os

# Create cache directory if it doesn't exist
temp_cache_dir = "f1_cache"
os.makedirs(temp_cache_dir, exist_ok=True)

# Enable caching for FastF1
fastf1.Cache.enable_cache(temp_cache_dir)

# Load F1 2024 Data
session_2024 = fastf1.get_session(2024, 3, "R")
session_2024.load()

# Extract lap times
laps_2024 = session_2024.laps[["Driver", "LapTime"]].copy()
laps_2024.dropna(subset=["LapTime"], inplace=True)
laps_2024["LapTime (s)"] = laps_2024["LapTime"].dt.total_seconds()

# Define drivers and qualifying times
qualifying_2025 = pd.DataFrame({
    "Driver": [
        "Lando Norris", "Oscar Piastri", "Max Verstappen", 
        "George Russell", "Yuki Tsunoda", "Alexander Albon",
        "Charles Leclerc", "Lewis Hamilton", "Pierre Gasly", "Carlos Sainz"
    ],
    "QualifyingTime (s)": [75.096, 75.180, 75.481, 75.546, 75.670,
                         75.737, 75.755, 75.973, 75.980, 76.062]
})

# Map driver names to codes
driver_mapping = {
    "Lando Norris": "NOR", "Oscar Piastri": "PIA", "Max Verstappen": "VER",
    "George Russell": "RUS", "Yuki Tsunoda": "TSU", "Alexander Albon": "ALB",
    "Charles Leclerc": "LEC", "Lewis Hamilton": "HAM", "Pierre Gasly": "GAS",
    "Carlos Sainz": "SAI"
}
qualifying_2025["DriverCode"] = qualifying_2025["Driver"].map(driver_mapping)

# Merge with 2024 data
merged_data = qualifying_2025.merge(laps_2024, left_on="DriverCode", right_on="Driver")
X = merged_data[["QualifyingTime (s)"]]
y = merged_data["LapTime (s)"]

# Train the model
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=39)
model.fit(X, y)

# Streamlit UI
st.title("🏎️ F1 2025 Race Prediction Dashboard 🏆")
st.markdown("Adjust the qualifying times to see how predictions change!")

# User Input Sliders
qual_times = []
st.sidebar.header("Adjust Qualifying Times")
for i, driver in enumerate(qualifying_2025["Driver"]):
    time = st.sidebar.slider(driver, 74.5, 77.0, qualifying_2025.loc[i, "QualifyingTime (s)"])
    qual_times.append(time)

# Update Qualifying Times
qualifying_2025["QualifyingTime (s)"] = qual_times

# Make Predictions
predicted_times = model.predict(qualifying_2025[["QualifyingTime (s)"]])
qualifying_2025["PredictedRaceTime (s)"] = predicted_times

# Rank Drivers by Predicted Race Time
qualifying_2025 = qualifying_2025.sort_values(by="PredictedRaceTime (s)")

# Display Results
st.header("🏆 Predicted Race Results")
st.dataframe(qualifying_2025[["Driver", "PredictedRaceTime (s)"]])

# Display Predicted Winner
winner = qualifying_2025.iloc[0]["Driver"]
st.success(f"🥇 Predicted Winner: {winner}")

# Evaluate Model
mae = mean_absolute_error(y, model.predict(X))
st.sidebar.metric(label="📉 Model Error (MAE)", value=f"{mae:.2f} seconds") 