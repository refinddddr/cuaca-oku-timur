import requests
import json

url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=16.08.03.2014"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False)[:5000])
