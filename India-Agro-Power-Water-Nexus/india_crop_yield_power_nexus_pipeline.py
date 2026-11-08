"""
India's Agro-Power-Water Nexus (2004-05 to 2024-25)
Econometric & Machine Learning Pipeline (RBI Handbook of Statistics on Indian States 2024-25)
Author: Manoj Chaandu Yeduvaka
"""
import numpy as np
import pandas as pd

STATE_2025_SNAPSHOT = [
    ("Punjab", "Northern", 4644, 98.8, 344.2, 2429, 2195, 11.2, 165.9),
    ("Haryana", "Northern", 4152, 94.0, 326.4, 2251, 3495, 13.0, 126.8),
    ("Tamil Nadu", "Southern", 3294, 59.8, 298.5, 1940, 19840, 13.8, 78.4),
    ("Telangana", "Southern", 3285, 62.4, 355.1, 2126, 5140, 14.1, 61.5),
    ("Andhra Pradesh", "Southern", 3157, 52.5, 343.0, 1482, 9419, 14.2, 29.8),
    ("West Bengal", "Eastern", 3128, 66.2, 285.4, 792, 690, 19.4, 45.2),
    ("Bihar", "Eastern", 3104, 64.0, 303.6, 344, 450, 25.8, 45.5),
    ("Uttar Pradesh", "Northern", 2958, 83.5, 292.1, 682, 5420, 21.6, 71.2),
    ("Gujarat", "Central/Western", 2545, 58.6, 241.0, 2310, 22480, 14.8, 66.8),
    ("Madhya Pradesh", "Central/Western", 2512, 68.4, 188.5, 1084, 6920, 22.4, 58.6),
    ("Uttarakhand", "Northern", 2498, 51.2, 210.4, 1612, 945, 16.4, 52.1),
    ("Chhattisgarh", "Central/Western", 2409, 32.2, 164.2, 1415, 1563, 22.2, 47.3),
    ("Kerala", "Southern", 2380, 24.5, 142.0, 935, 1120, 12.8, 51.4),
    ("Assam", "North-Eastern", 2221, 17.0, 94.9, 356, 192, 17.6, 12.6),
    ("Odisha", "Eastern", 2195, 36.8, 138.4, 1245, 1150, 21.0, 44.2),
    ("Himachal Pradesh", "Northern", 2140, 22.8, 118.5, 1540, 1110, 13.5, 38.4),
    ("Karnataka", "Southern", 2065, 39.4, 215.0, 1390, 18450, 14.6, 69.5),
    ("Jharkhand", "Eastern", 1982, 16.8, 98.2, 718, 165, 29.8, 31.2),
    ("Maharashtra", "Central/Western", 1745, 26.4, 192.4, 1560, 14820, 17.8, 54.8),
    ("Rajasthan", "Northern", 1692, 44.5, 112.6, 1410, 26850, 21.5, 148.2),
]

def run_summary():
    cols = [
        "State", "Region", "Foodgrain_Yield_kg_ha", "Irrigation_Coverage_Pct",
        "Fertiliser_kg_per_ha_NSA", "Per_Capita_Power_kWh", "Renewable_Capacity_MW",
        "TD_Losses_Pct", "Groundwater_Extraction_Pct"
    ]
    df = pd.DataFrame(STATE_2025_SNAPSHOT, columns=cols)
    print("=== 2024-25 State-Wise Agro-Power-Water Cross-Section (N=20 States) ===")
    print(df.to_string(index=False))
    print("\nMean Foodgrain Yield (kg/ha):", round(df["Foodgrain_Yield_kg_ha"].mean(), 1))
    print("Mean Groundwater Extraction (%):", round(df["Groundwater_Extraction_Pct"].mean(), 1))

if __name__ == "__main__":
    run_summary()
