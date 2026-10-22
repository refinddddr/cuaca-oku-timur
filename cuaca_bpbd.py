import json
import os
import requests

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
sheet = spreadsheet.worksheet("Status_BPBD")

url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=16.08.03.2014"

r = requests.get(url)

data = r.json()

lokasi = data["lokasi"]

cuaca = "TIDAK DIKETAHUI"
suhu = ""
kelembaban = ""

try:
    prakiraan = data["data"][0]["cuaca"][0][0]

    cuaca = prakiraan["weather_desc"]
    suhu = prakiraan["t"]
    kelembaban = prakiraan["hu"]

except Exception:
    pass

status_bpbd = "NORMAL"

if "Ringan" in cuaca:
    status_bpbd = "WASPADA"

if "Sedang" in cuaca:
    status_bpbd = "SIAGA"

if "Lebat" in cuaca:
    status_bpbd = "AWAS"

if "Petir" in cuaca:
    status_bpbd = "AWAS"

from datetime import datetime

sheet.append_row([
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    lokasi["kecamatan"],
    lokasi["desa"],
    lokasi["adm4"],
    cuaca,
    suhu,
    kelembaban,
    status_bpbd
])
print("Data BPBD berhasil ditulis")
