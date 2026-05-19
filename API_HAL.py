import requests
import json

startUrl = "https://api.archives-ouvertes.fr/search/?q=("

ensData = []

try:
    with open('enseignants.json', 'r') as file:
        ensData = json.load(file)

    articlesData = []

    for ensJSON in ensData:

        response = requests.get(startUrl+ensJSON["nom"]+")")
        infos = response.json()

        for elt in infos["response"]["docs"]:
            elt = elt["label_s"].split(". ")
            articleName = elt[1]

            exists = False

            for articleJSON in articlesData:
                if articleName==articleJSON["article"]:
                    exists = True
            if not exists:
                coAuth = elt[0].split(", ")
                articlesData.append({"article":articleName,"authors":coAuth})

    with open("articlesCoAuteurs_HAL.json", "wt+", newline="", encoding="utf-8") as f:
        json.dump(articlesData, f, ensure_ascii=False, indent=4)


except FileNotFoundError:
    print("Error: Fichier 'enseignants.json'.")
