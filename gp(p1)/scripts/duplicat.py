import pandas as pd

SMS_FILE = r"C:\Users\kavya\OneDrive\Desktop\gp\input\smsbackup.xlsx"

print("Removing duplicates from:", SMS_FILE)

df = pd.read_excel(SMS_FILE)

print("Rows before:", len(df))

df = df.drop_duplicates().reset_index(drop=True)

print("Rows after:", len(df))

df.to_excel(SMS_FILE, index=False)

print("Duplicates removed successfully")