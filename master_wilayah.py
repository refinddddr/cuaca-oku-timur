import json
import os

from google.oauth2.service_account import Credentials
import gspread

# Google Sheet Auth
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
sheet = spreadsheet.worksheet("Master_Wilayah")

# Bersihkan sheet
sheet.clear()

# Header
sheet.append_row([
    "kecamatan",
    "desa_kelurahan",
    "kode_wilayah"
])

# Contoh data awal
data = [
    ["Belitang", "Gumawang", "16.08.03.2003"],
    ["Belitang", "Karang Kemiri", "16.08.03.2004"],
    ["Belitang", "Mojosari", "16.08.03.2005"],
    ["Buay Madang", "Tebat Jaya", "16.08.02.2016"],
]

for row in data:
    sheet.append_row(row)

print("Master_Wilayah berhasil dibuat")
