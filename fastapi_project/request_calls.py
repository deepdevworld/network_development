import json
import requests



url = "http://127.0.0.1:8000/"
endpoint = "items/"
header = {"content-type": "application/json"}
response = requests.get(url=url+endpoint, params={"skip": 0, "limit": 2}, headers=header)
print(response.json())