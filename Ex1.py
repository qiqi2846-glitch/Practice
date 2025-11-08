#%% - import
import requests as rq
import json

#%% - Get data
url = "https://fakestoreapi.com/products"
response = rq.get(url)

#%% - Display data
data = response.json()
print(data)

#%% - Save data
with open("data/products.json", "w", encoding="utf8") as f:
    json.dump(data, f, indent=3)