import fastf1
import pandas as pd
import numpy as np

print("Starting test...")

# Enable caching for FastF1
print("Setting up cache...")
temp_cache_dir = "f1_cache"
fastf1.Cache.enable_cache(temp_cache_dir)

# Load F1 2024 Data
print("Loading session data...")
session_2024 = fastf1.get_session(2024, 3, "R")
print("Session loaded, now loading data...")
session_2024.load()
print("Data loaded successfully!")

# Extract lap times
print("Extracting lap times...")
laps_2024 = session_2024.laps[["Driver", "LapTime"]].copy()
laps_2024.dropna(subset=["LapTime"], inplace=True)
laps_2024["LapTime (s)"] = laps_2024["LapTime"].dt.total_seconds()
print("Lap times extracted successfully!")

print("\nSample of lap times:")
print(laps_2024.head())

print("\nTest completed successfully!") 