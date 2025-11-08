#%% - import Lib
import xmltodict as xm
import json

#%% -
with open("data/products.xml", "r", encoding="utf8") as f:
    json_obj = xm.parse(f.read())
    #print(json_obj)
    #temp = json.dumps(json_obj, indent=3) #str
    product_list = json_obj["products"]["product"]
    print(product_list)
    #Save data --> (beers.json) json file
    with open("data/beers.json", "w", encoding="utf8") as json_f:
        json.dump(product_list, json_f, indent=3)
