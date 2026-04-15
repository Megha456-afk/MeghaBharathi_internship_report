
import pandas as pd
import os

# go to gp folder instead of scripts folder
BASE_DIR = r"C:\Users\kavya\OneDrive\Desktop\gp"

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEXT_DIR = os.path.join(BASE_DIR, "text")

FINAL_FILE = os.path.join(OUTPUT_DIR, "FINAL_SORTED_03022026.xlsx")
SMS_FILE = os.path.join(INPUT_DIR, "smsbackup.xlsx")
GP_MASTER = os.path.join(INPUT_DIR, "KDAH Indore GP master file.xlsx")
CONFIG_FILE = os.path.join(TEXT_DIR, "config.txt")


def gp_merge():
    print("\n Merging GP master...")

    gp_master = pd.read_excel(GP_MASTER, dtype=str)
    final_sorted = pd.read_excel(FINAL_FILE, dtype=str)

    gp_master.columns = gp_master.columns.str.strip()
    final_sorted.columns = final_sorted.columns.str.strip()

    gp_master["PH_NO"] = gp_master["PH_NO"].str.strip()
    final_sorted["PH_NO"] = final_sorted["PH_NO"].str.strip()

    cols = [
        "REFERRING_DOCTOR", "AREA", "AREA_MANAGER",
        "SALES_MANAGER", "VENDOR_CODE", "PAN_NO",
        "VENDOR_NAME", "SPECIALTY"
    ]

    merged = final_sorted.merge(
        gp_master[["PH_NO"] + cols],
        on="PH_NO",
        how="left",
        suffixes=("", "_gp")
    )

    for col in cols:
        merged[col] = merged[col].fillna(merged[col + "_gp"])
        merged.drop(columns=[col + "_gp"], inplace=True)

    merged.to_excel(FINAL_FILE, index=False)

def extract_date_time():
    print("\n Extracting date/time...")

    df = pd.read_excel(FINAL_FILE, dtype=str)

    temp_dt = pd.to_datetime(
        df["SMS_DATE"],
        format="%Y-%m-%d %a %I:%M %p",
        errors="coerce"
    )

    df.loc[temp_dt.notna(), "S_DATE"] = temp_dt.dt.strftime("%Y-%m-%d")
    df.loc[temp_dt.notna(), "S_TIME"] = temp_dt.dt.strftime("%H:%M")

    df.to_excel(FINAL_FILE, index=False)

    print(" Date/time extracted")


def fill_blanks():
    print("\n Filling blanks...")

    df = pd.read_excel(FINAL_FILE, dtype=str)
    df = df.fillna("NOT_MAPPED")
    df.replace("", "NOT_MAPPED", inplace=True)

    df.to_excel(FINAL_FILE, index=False)

    print("Blank fill complete")



    # ===== SL_NO AUTO FILL =====

    sl_numeric = pd.to_numeric(df["SL.NO"], errors="coerce")

    # get last valid serial number safely
    last_sl = int(sl_numeric.max()) if sl_numeric.notna().any() else 0

    for i in df.index:
        if pd.isna(sl_numeric[i]):
            last_sl += 1
            df.at[i, "SL.NO"] = last_sl

    # save updated file
    df.to_excel(FINAL_FILE, index=False)



gp_merge()
extract_date_time()
fill_blanks()