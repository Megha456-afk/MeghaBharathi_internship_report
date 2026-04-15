import pandas as pd
import random

rows = []

for i in range(5000):

    rainfall = random.randint(0, 200)          # mm
    temperature = random.uniform(18, 45)       # °C
    humidity = random.randint(15, 100)         # %
    soil_moisture = random.randint(5, 60)      # %
    wind_speed = random.randint(0, 35)         # km/h

    # Drought rule logic
    drought_score = 0

    if rainfall < 50:
        drought_score += 1
    if soil_moisture < 25:
        drought_score += 1
    if temperature > 35:
        drought_score += 1
    if humidity < 35:
        drought_score += 1
    if wind_speed > 20:
        drought_score += 1

    drought = 1 if drought_score >= 3 else 0

    rows.append([
        round(rainfall,2),
        round(temperature,2),
        humidity,
        soil_moisture,
        wind_speed,
        drought
    ])

columns = [
    "rainfall",
    "temperature",
    "humidity",
    "soil_moisture",
    "wind_speed",
    "drought"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("dataset/drought_data.csv", index=False)

print("✅ 5000-row drought dataset created!")
print(df.head())