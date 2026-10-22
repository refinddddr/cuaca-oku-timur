import requests

url = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4=16.08.03.2014"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text[:500])
