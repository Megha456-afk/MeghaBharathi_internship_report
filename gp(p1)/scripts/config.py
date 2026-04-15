import pandas as pd
import os

# FIXED base directory (important for Automation Anywhere)
BASE_DIR = r"C:\Users\kavya\OneDrive\Desktop\gp"

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEXT_DIR = os.path.join(BASE_DIR, "text")

FINAL_FILE = os.path.join(OUTPUT_DIR, "FINAL_SORTED_03022026.xlsx")
SMS_FILE = os.path.join(INPUT_DIR, "smsbackup.xlsx")
GP_MASTER = os.path.join(INPUT_DIR, "KDAH Indore GP master file.xlsx")
CONFIG_FILE = os.path.join(TEXT_DIR, "config.txt")

def config_filter():
    print("\n Applying checkpoint filter...")
    print("SMS file:", SMS_FILE)
    print("Final file:", FINAL_FILE)
    print("Config file:", CONFIG_FILE)

    with open(CONFIG_FILE, "r") as f:
        checkpoint_str = f.readline().split("=")[1].strip()

    checkpoint = pd.to_datetime(
        checkpoint_str,
        format="%Y-%m-%d %a %I:%M %p",
        errors="coerce"
    )

    data = pd.read_excel(SMS_FILE)
    data.columns = data.columns.str.strip().str.lower()

    data["date"] = pd.to_datetime(
        data["date"],
        format="%Y-%m-%d %a %I:%M %p",
        errors="coerce"
    )

    data = data.dropna(subset=["date"])

    new_records = data[data["date"] > checkpoint].sort_values("date")

    mapped = new_records[["address", "date", "body"]].copy()
    mapped.columns = ["PH_NO", "SMS_DATE", "SMS_BODY"]
    mapped["SMS_DATE"] = mapped["SMS_DATE"].dt.strftime(
        "%Y-%m-%d %a %I:%M %p"
    )

    try:
        final_df = pd.read_excel(FINAL_FILE, dtype=str)
    except FileNotFoundError:
        final_df = pd.DataFrame(columns=mapped.columns)

    updated = pd.concat([final_df, mapped], ignore_index=True)

    updated.to_excel(FINAL_FILE, index=False)

    print("Rows added:", len(mapped))
    print("Total rows in final:", len(updated))
    print(" Config merge complete")

config_filter()