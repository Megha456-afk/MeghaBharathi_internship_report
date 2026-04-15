import pandas as pd

# read file — keep everything as text
df = pd.read_excel("FINAL_SORTED_03022026.xlsx", dtype=str)

# temporary datetime conversion
temp_dt = pd.to_datetime(
    df["SMS_DATE"],
    format="%Y-%m-%d %a %I:%M %p",
    errors="coerce"
)

# fill S_DATE only where valid
df.loc[temp_dt.notna(), "S_DATE"] = temp_dt.dt.strftime("%Y-%m-%d")

# fill S_TIME only where valid
df.loc[temp_dt.notna(), "S_TIME"] = temp_dt.dt.strftime("%H:%M")

# save — no rows removed
df.to_excel("FINAL_SORTED_03022026.xlsx", index=False)

print("✅ S_DATE and S_TIME filled — all records preserved!")
