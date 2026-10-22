import requests

url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=16.08.01.2001"

response = requests.get(url)

print(response.status_code)

with open("sample.json", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Data berhasil diambil")
