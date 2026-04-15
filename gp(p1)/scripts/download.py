import requests

SPREADSHEET_ID = "1zxIuyxjE3ctoHdkxB_uvV_liN9iS2aTR"

url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=xlsx"

session = requests.Session()

response = session.get(url)

print("Status:", response.status_code)

if response.status_code == 200:
    with open(r"C:\Users\kavya\OneDrive\Desktop\gp\input\smsbackup.xlsx", "wb") as f:
        f.write(response.content)
    print("Downloaded successfully")
else:
    print("Download failed")