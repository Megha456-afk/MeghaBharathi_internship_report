import pandas as pd

# Load both Excel files
file1 = pd.read_excel("smsbackup_cleaned_file.xlsx")
file2 = pd.read_excel("KDAH Indore GP master file.xlsx")

# Select columns you want
file1_cols = file1[["Address","Date", "Body"]]     # change as needed
file2_cols = file2[["REFERRING_DOCTOR","AREA","AM","AREA_MANAGER","VENDOR_CODE","PAN_NO","SPECIALTY","SALES_MANAGER",]]  # change as needed

# Combine side by side
combined = pd.concat([file1_cols, file2_cols], axis=1)

# Save result
combined.to_excel("final_sort.xlsx", index=False)

print("✅ Columns extracted and combined successfully!")
