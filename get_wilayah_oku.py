import requests

url = "https://raw.githubusercontent.com/cahyadsn/wilayah/master/data/list_desa.csv"

r = requests.get(url)

print(r.status_code)
print(r.text[:1000])
