import requests
import json

startUrl = "https://api.archives-ouvertes.fr/search/?q=("
endUrl = ")"
ensName = "flavien vernier"

data = []

response = requests.get(startUrl+ensName+endUrl)
infos = response.json()

for elt in infos["response"]["docs"]:
    elt = elt["label_s"].split(". ")
    coAuth = elt[0].split(", ")
    
    data.append({"article":elt[1],"authors":coAuth})


with open("articlesCoAuteurs_HAL.json", "wt+", newline="", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)