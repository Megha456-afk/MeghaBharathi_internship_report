import pandas as pd

# Load your Excel file
df = pd.read_excel("FINAL_SORTED_03022026.xlsx", dtype=str)

# Replace blanks / empty cells with NOT_MAPPED
df = df.fillna("NOT_MAPPED")
df.replace("", "NOT_MAPPED", inplace=True)

# Save back to Excel
df.to_excel("FINAL_SORTED_03022026.xlsx", index=False)

print("✅ All blank cells filled with NOT_MAPPED")
