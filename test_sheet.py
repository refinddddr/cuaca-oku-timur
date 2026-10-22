import json
import os
from google.oauth2.service_account import Credentials
import gspread

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=scope
)

client = gspread.authorize(creds)

spreadsheet = client.open("Data Cuaca OKU Timur")
sheet = spreadsheet.sheet1

sheet.append_row([
    "TEST",
    "Koneksi Berhasil"
])

print("Sukses menulis ke Spreadsheet")
