import pandas as pd

df=pd.read_excel("final_output.xlsx")

df.columns=["PH_NO","S_DATE","SMS_BODY","SL.NO","REFERRING_DOCTOR","AREA","AREA_MANAGER","VENDOR_CODE","PAN_NO","SPECIALTY","SALES_MANAGER"]
print(df.columns)

df.to_excel("final_output.xlsx", index=False)