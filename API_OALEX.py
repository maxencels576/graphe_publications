import requests
import json
import time

API_AUTHORS = "https://api.openalex.org/authors"

def chargerEnseignant(path="enseignants.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def trouverAuteur(name):
    params = {"search": name}
    r = requests.get(API_AUTHORS, params=params)
    r.raise_for_status()
    results = r.json().get("results", [])
    return results[0] if results else None

def getTravailAuteur(works_api_url):
    r = requests.get(works_api_url)
    r.raise_for_status()
    return r.json().get("results", [])

def getArticleInfo(work):
    title = work.get("title")
    authors = [a["author"]["display_name"] for a in work.get("authorships", [])]
    return title, authors


enseignants = chargerEnseignant()
articles = []

for ens in enseignants:
    name = ens["nom"]
    print(f"Recherche OpenAlex : {name}")
    author = trouverAuteur(name)

    if not author:
        print(f"Aucun auteur trouvé pour {name}")
        continue

    works_url = author["works_api_url"]
    works = getTravailAuteur(works_url)

    for w in works:
        title, authors = getArticleInfo(w)
        if not title:
            continue

        if not any(a["article"] == title for a in articles):
            articles.append({
                "article": title,
                "authors": authors
            })

    time.sleep(0.2)

with open("articlesCoAuteurs_OpenAlex.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)


